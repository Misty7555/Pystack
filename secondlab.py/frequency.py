list1 = [1, 2, 3, 4, 5, 6, 2]

for i in list1:
    count = 0
    for j in list1:
        if i == j:
            count += 1
    print("Frequency of", i, "=", count)
