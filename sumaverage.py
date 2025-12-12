# Program to find sum and average of n numbers
n = int(input("Enter how many numbers: "))
total = 0
for i in range(n):
    num = float(input(f"Enter number {i+1}: "))
    total += num
average = total / n
print("Sum of the numbers is:", total)
print("Average of the numbers is:", average)