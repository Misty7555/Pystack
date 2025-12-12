lst = [1,2,3,4,5,6,7,8,9,10]

largest = -999999
second_largest = -999999

smallest = 999999
second_smallest = 999999

# Find largest & second largest
for i in lst:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i != largest:
        second_largest = i

print("Largest number is:", largest)
print("Second largest number is:", second_largest)

# Find smallest & second smallest
for i in lst:
    if i < smallest:
        second_smallest = smallest
        smallest = i
    elif i < second_smallest and i != smallest:
        second_smallest = i

print("Smallest number is:", smallest)
print("Second smallest number is:", second_smallest)
