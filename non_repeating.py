def non_repeating(string):
    count = {}

    for i in string:
        if i not in count:
            count[i]=1
        else:
            count[i]+=1
    for i in count:
        return count.keys(i), count.values(i)
    #return False
    print(non_repeating("google"))


    