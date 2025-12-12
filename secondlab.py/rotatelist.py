list1 = [1, 2, 3, 4, 5, 6]
pos = int(input("Enter rotation position: "))
pos = pos % len(list1) 
rotated_list = list1[-pos:] + list1[:-pos]
print("Original List:", list1)
print("After Clockwise Rotation:", rotated_list)
