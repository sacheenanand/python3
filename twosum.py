def twosum(list, target):
    list = [1,2,3,4,5]
    target = 5

    beg, end = 0, len(list)-1

    while beg < end:
        if (list[beg] + list[end]) == target:
            return [beg+1, end+1]
        elif (list[beg] + list[end]) > target:
            end -= 1
        else:
            beg +=1
print(twosum([1,2,3,4,5], 3))