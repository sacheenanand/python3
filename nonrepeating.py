def nonrepeating(string):
    count = {}
    list = []

    for i in string:
        if i not in count:
            count[i]=1
            list.append(i)
        else:
            count[i]+=1
    print(count)
    print(list)

    for k in count.keys():
        if count[k]==1:
            return k
    return False
print(nonrepeating("google"))




'''for k,v in list:
        if count[k] == 1:
            return k
    return False

print(nonrepeating("google"))
'''


