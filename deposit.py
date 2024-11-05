balance = 45.67

while True:
    try:
        num = float(input(" enter the balance: "))
        break
    except ValueError:
        print("must be valid number")



balance += num

print("here is the balance", balance)

