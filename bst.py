# binary tree , put all the nodes in list . Binary Tree to list 
# using depth first search (recurcive)

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.left = None
        self.right = None


def treeToListHelper(root, result, level):
    if root is None:
        return 
    
    if level ==len(result):
        new_list = []
        result.append(new_list)
    else:
        new_list = result[level]
    new_list.append(root.data)
    treeToListHelper(root.left, result, level+1)
    treeToListHelper(root.right, result, level+1)


def TreetoList(root):
    result = []
    treeToListHelper(root, result, 0)
    return result




