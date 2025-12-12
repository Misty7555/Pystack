n = int(input("Enter how many numbers: "))
largest = -999999
second_largest = -999999
for i in range(n):
    num = int(input("Enter number: "))
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num
        print("Largest number is:", largest)
print("Second largest number is:", second_largest)
