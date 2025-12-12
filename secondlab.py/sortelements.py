list = [5,6,7,8]
for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[j] < list[i]:
            list[i],list[j] = list[j],list[i]
print("Sorted list:", list)
