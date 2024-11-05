#python to remove duplicates in a string.

def duplicates(string):
    empty_string = ""
    for i in string:
        if i not in empty_string:
            empty_string+=i
        else:
            pass
    return empty_string
print(duplicates("helloheeellmm"))


        
