def calculator():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    ch = int(input("1.Add 2.Sub 3.Mul 4.Div : "))

    if ch == 1:
        print(a + b)
    elif ch == 2:
        print(a - b)
    elif ch == 3:
        print(a * b)
    elif ch == 4:
        print(a / b)

calculator()
