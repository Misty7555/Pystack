tup = (1,2,3,4,5,6,7,8,9,10)
largest = -999999
second_largest = -999999
smallest = 999999
second_smallest = 999999
for i in tup:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i != largest:
        second_largest = i
print("Second largest number is:", second_largest)
for i in tup:
    if i < smallest:
        second_smallest = smallest
        smallest = i
    elif i < second_smallest and i != smallest:
        second_smallest = i
print("Second smallest number is:", second_smallest)
