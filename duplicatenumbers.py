def duplicatenumbers(list):
    result = []
    b = {}

    for element in list:
        if element in b:
            b[element] += 1
        else:
            b[element] = 1
    
    for e, v in b.items():
        x = 1
        #print(b[e])
        #print(b[v])
        if b[e]>x:
            result.append(e)
    return result
print(duplicatenumbers([1,2,5,5,9,9,2,1]))