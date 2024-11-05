'''
reverse a string 
'''


def reversestring(str):
       if len(str)==0:
           return str
       else:
          return reversestring(str[1:]) + str[0]
print(reversestring("abcdefghi"))


name = 'sacheen'
name = 'anand'
print(name)




