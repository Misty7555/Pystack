tup = (5, 2, 8, 1, 9, 3)
lst = list(tup)
n = 0
for _ in lst:
    n += 1
for i in range(n):
    for j in range(i + 1, n):
        if lst[i] > lst[j]:
            temp = lst[i]
            lst[i] = lst[j]
            lst[j] = temp
sorted_tup = tuple(lst)
print("Sorted tuple:", sorted_tup)
