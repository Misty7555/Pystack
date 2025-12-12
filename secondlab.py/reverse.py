list = [1,2,3,4,5,6]
reversed_list = []
for i in range(len(list)-1, -1,-1):
    reversed_list.append(list[i])
print("The reversed list is:", reversed_list)