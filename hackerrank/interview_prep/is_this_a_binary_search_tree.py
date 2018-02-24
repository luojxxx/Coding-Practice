# https://www.hackerrank.com/challenges/ctci-is-binary-search-tree
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def check(node, depth = 0):
    if node.left != None and node.right != None:
        stateLeft, valMinLeft, valMaxLeft = check(node.left )
        stateRight, valMinRight, valMaxRight = check(node.right )
        newState = None
        if stateLeft == False or stateRight == False:
            newState = False
        elif valMaxLeft < node.data and valMinRight > node.data:
            newState = True
        else:
            newState = False
        return [newState, min(valMinLeft, valMinRight, node.data), max(valMaxLeft, valMaxRight, node.data)]

    if node.left != None and node.right == None:
        state, valMin, valMax = check(node.left)
        newState = None
        if state == False:
            newState = False
        elif valMax < node.data:
            newState = True
        else:
            newState = False
        return [newState, min(valMin, node.data), max(valMax, node.data)]

    if node.left == None and node.right != None:
        state, valMin, valMax = check(node.right)
        newState = None
        if state == False:
            newState = False
        elif valMin > node.data:
            newState = True
        else:
            newState = False
        return [newState, min(valMin, node.data), max(valMax, node.data)]

    if node.left == None and node.right == None:
        return [True, node.data, node.data]

def check_binary_search_tree_(root):
    #optimal finds the min, max at each node
    state, _, _  = check(root)
    return state