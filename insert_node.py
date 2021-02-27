def insert_node(value,tree):  #value: ['frontframe', (1, 'fork'), (2, 'handle')]
    if type(datum(tree)) != list:
        print("datum",datum(tree))
        print(1)
        return
    elif value[0] in datum(tree): 
        print(datum(tree))
        for x in value[1:]:
            tree.append([list(x)])
    elif is_leaf(tree):
        print(2)
        return 
    else:
        print(3)
        return insert_helper(value,children(tree))  



def insert_helper(value,tree):
    if len(tree) == 0:
        print(4)
        return 
    else:
        print(5)
        print(tree)
        return insert_node(value,tree[0]) , insert_helper(value,tree[1:])
    


def is_exist(value,t):
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



def datum(t):
    return t[0]

def children(t):
    return t[1:]

def is_leaf(t):
    return len(children(t)) == 0

def is_empty(t):
    return t == []


tree = [[1, 'bike'], [[2,'wheel']], [[2,'frame']]]
value = ["wheel",(3,"fork"),(4,"ben")]
"""
insert_node(value,tree)
print(tree)
"""
print(is_exist("wheel",tree))
