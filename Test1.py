def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
num1 = int(input("enter a num:  "))
num2 = int(input("enter a num:  "))
print(gcd(num1, num2))



