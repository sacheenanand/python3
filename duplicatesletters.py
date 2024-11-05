'''
To delete a duplicates letters in string
'''

def duplic(str):
    empty = ""
    for char in str:
        if char not in empty:
            empty += char
    return empty
print(duplic("xyzzzyxxxxxxxxx"))
