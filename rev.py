def rev(string):
    if len(string)==0:
        return string
    else:
        return rev(string[1:])+ string[0]
q= str(input("Enter a string to be reversed:  "))
print(rev(q))

