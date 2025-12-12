list = [1, "python", 2 , 1 , "c" , 3 , 2 , "python"]
new_list = []
for i in list:
    if i not in new_list:
        new_list.append(i)
print ("New list without duplicates: ", new_list)