# find the index of the occurence in substring 

def substring(str):
    str = "hello"
    needle = "ll"
    for i in range(len(str)+1 - len(needle)):
        if str[i:i+len(needle)]==needle:
            return i
    return -1
print(substring(str))
