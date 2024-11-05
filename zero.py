# to program the list of numbers and move zero to the end of the list

def zero(list):

    for item in list:
        if item == 0:

            list.remove(item)
            list.append(item)
    return list
print(zero([1,0,2,3,4]))