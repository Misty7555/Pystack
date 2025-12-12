list = [1,2,3,4,5]
n = int(input("Enter the item to be deleted: "))
new_list = []
for i in list:
    if i != n:
        new_list.append(i)
print ("new list: ",n,":" ,new_list)