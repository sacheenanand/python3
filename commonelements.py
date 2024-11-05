list1 = [10,20,30,40,70]
list2=[10,50,60,70]

def commonele(list1, list2):
    p1 = 0
    p2 = 0
    result = []

    while p1<len(list1) and p2<len(list2):
        if list1[p1] == list2[p2]:
            result.append(list1[p1])
            p1+=1
            p2+=1
        elif list1[p1]>list2[p2]:
            p2+=1
        else:
            p1+=1
    return result
print(commonele(list1, list2))

        

