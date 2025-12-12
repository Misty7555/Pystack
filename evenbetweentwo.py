start = int(input("Enter first number: "))
end = int(input("Enter second number: "))
for num in range(start, end - 1, -1):
    if num % 2 == 0:
        print(num)