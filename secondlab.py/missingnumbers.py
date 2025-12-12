list = [1,2,4,6]
print("Missing number", end=" ")
for i in range(min(list),max(list)):
    if i not in list:
        print(i,end=" ")
