'''
valid parenthesis

str = '{(]}
'''

def isvalidparenthesis(str):
    d = {'(':')', '{':'}', '(':')', '[':']'}
    stack = []

    for i in str:
        if i in d:
            stack.append(i)
            print(stack)
        elif stack == [] or d[stack.pop()]!=i:
            return False
    return stack == [] 

#print(isvalidparenthesis('{()}'))
print(isvalidparenthesis('{([(()}])}'))


            

