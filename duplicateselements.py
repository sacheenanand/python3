def duplicates(list):
    result = []
    for element in list:
        if list.count(element)>1 and element not in result:
            result.append(element)
    return result
print(duplicates([1,2,2,3,4,4,5]))