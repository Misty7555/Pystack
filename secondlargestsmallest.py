def second_smallest_largest(lst):
    lst.sort() 
    print("Second Smallest:", lst[1])
    print("Second Largest:", lst[-2])
n = int(input("Enter number of elements: "))
lst = [int(input("Enter element: ")) for _ in range(n)]
second_smallest_largest(lst)