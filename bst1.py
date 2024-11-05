def ListToBinary(root, result, level):
    if root is None:
        return
    
    if level == len(result):
        new_list = []
        result.append(new_list)
    else:
        new_list = result[level]
    new_list.append(root.data)
    ListToBinary(root.left, result, level+1)
    ListToBinary(root.right, result, level+1)








