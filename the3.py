#Arda Numanoglu METU

def splitter(part_list): #divides part_list into "prices of basic parts" and "tree elements"
    prices = list()
    tree_elements = list()
    for x in part_list:
        if type(x[1]) != tuple:
            prices.append(x)
        else:
            tree_elements.append(x)
    return tree_elements,prices

def root_finder(tree_elements): #Finds the prospective tree-root of given part_list
    if len(tree_elements) == 0:
        return []
    values = list()
    for x in tree_elements:
        values.append(x[0])
    i = 0
    for k in values:
        if any(k in s1 for s1 in tree_elements[:i]+tree_elements[i+1:]) or any(any(k in s2 for s2 in s1[1:]) for s1 in tree_elements[:i]+tree_elements[i+1:]):
            i+=1
            continue
        else:
            return [values[i]] #returns the root! sample: ["bike"]
    
def tree_maker(part_list): #makes a tree! 
    tree = list()          #sample tree: [[1, 'bike'], [[2, 'wheel'], [[1, 'rim', 60.0]], [[1, 'spoke', 120.0]], [[1, 'hub'], [[2, 'gear', 25.0]], [[1, 'axle'], [[5, 'bolt', 0.1]], [[7, 'nut', 0.15]]]]], [[1, 'frame'], [[1, 'rearframe', 175.0]], [[1, 'frontframe'], [[1, 'fork', 22.5]], [[2, 'handle', 10.0]]]]] 
    queue = list()
    if root_finder(splitter(part_list)[0]) == []: #checks if it s a 1 node tree or not.
        __a = splitter(part_list)[1]
        __a = __a[0]
        return [[1]+list(__a)]
    root = root_finder(splitter(part_list)[0])[0]
    prices = splitter(part_list)[1]
    for elem in splitter(part_list)[0]:
        queue.append(elem)

    for is_root in queue:
        if is_root[0] == root:
            tree = [[1,is_root[0]]]
            for child in is_root[1:]:
                tree.append([[child[0],child[1]]])
            queue.remove(is_root)    
    while queue:
        top = queue.pop(0)
         # top: ['frontframe', (1, 'fork'), (2, 'handle')]
        if is_exist(top[0],tree):
            insert_node(top,tree)
        else:
            queue.append(top)  

    price_adder(tree,prices)
    return tree 


################################################################

def calculate_price(part_list): #Function1
    
    tree = tree_maker(part_list)
    return calculate_helper(tree)
    

def calculate_helper(tree):
    if is_leaf(tree):
        return datum(tree)[2]
    else:
        return calculate_forest(children(tree))

def calculate_forest(tree):
    if len(tree) == 0:
        return 0
    else:
        return datum(tree[0][0])*calculate_helper(tree[0]) + calculate_forest(tree[1:])

##################################################################

def required_parts(part_list): #Function2
    
    tree = tree_maker(part_list)
    output = list()
    return output + required_parts_helper(tree) 
    

def required_parts_helper(tree,count = 1):
    if is_leaf(tree):
        return [tuple([count*datum(tree[0]),datum(tree)[1]])]
    else:
        return required_parts_helper_forest(children(tree),count*datum(tree[0]))

def required_parts_helper_forest(tree,count):
    if len(tree) == 0:
        return []
    else:
        return required_parts_helper(tree[0],count) + required_parts_helper_forest(tree[1:],count)

##################################################################

def stock_check(part_list,stock_list): #Function3
    
    required = required_parts(part_list)
    output = list()
    queue = list()
    for elem in required:
        queue.append(elem)
    
    while queue:
        front = queue.pop(0)
        if front in stock_list:
            continue
        elif any(front[1] in i for i in stock_list):
            for j in stock_list:
                if front[1] == j[1] and j[0]<front[0]:
                    amount = front[0]-j[0]
                    output.append(tuple([front[1],amount]))
                    continue
                elif front[1] == j[1] and front[0]<j[0]:
                    break
        else:
            output.append(tuple([front[1],front[0]]))
    return output
    
##################################################################

""" TREE FUNCTIONS """

def datum(t):
    return t[0]

def children(t):
    return t[1:]

def is_leaf(t):
    return len(children(t)) == 0

def is_empty(t):
    return t == []

def is_exist(value,t): #checks if a value exists in the tree or not
    if type(datum(t)) != list:
        return False
    elif value in datum(t):
        return True
    elif is_leaf(t):
        return False
    else:
        return is_exist_helper(value,children(t))


def is_exist_helper(value,t):
    if len(t) == 0:
        return False
    else:
        return is_exist(value,t[0]) or is_exist_helper(value,t[1:])

def insert_node(value,tree): #inserts a value to a tree!  #value sample: ['frontframe', (1, 'fork'), (2, 'handle')]
    
    if type(datum(tree)) != list:
        return
    elif value[0] in datum(tree): 
        for x in value[1:]:
            tree.append([list(x)])
    elif is_leaf(tree):
        return 
    else:
        return insert_helper(value,children(tree))  

def insert_helper(value,tree):
    if len(tree) == 0:
        return 
    else:
        return insert_node(value,tree[0]) , insert_helper(value,tree[1:])
    
def price_adder(tree,prices): #inserts the prices to the leafs of tree 
    if type(datum(tree)) != list:
        return
    elif any(datum(tree)[1] in p for p in prices):
        for i in prices:
            if i[0] == datum(tree)[1]:
                cost = i[1]
                datum(tree).append(cost)
    elif is_leaf(tree):
        return 
    else:
        return price_adder_helper(children(tree),prices) 
def price_adder_helper(tree,prices):
    if len(tree) == 0:
        return
    else:
        return price_adder(tree[0],prices) , price_adder_helper(tree[1:],prices)