import math 

x = 10
y = 4

ans = math.gcd(x,y)
print(ans)



def gcd(x,y):
    if y == 0:
        return x 
    else:
        return gcd(y, x%y)
print(gcd(100,3))
print(gcd(4,18))
print(gcd(64,48))


