def datum(T):
	return T[0]

def isempty(T):
	return T == []

def left(T):
	return T[1]

def right(T):
	return T[2]

def createNode(datum, left = None , right = None):
	return [datum, left if left else [] , right if right else []]

#########################################################################


def insert_node(T, value):
	if isempty(T):
		T.extend(createNode(value))
	elif( datum(T) == value ): #duplicate
		return
	elif value < datum(T):
		insert_node(left(T) , value)
	else:
		insert_node(right(T), value)


