list = [1,2,3,4,5,6,7,8,-1,-2]
positive_list = []
negative_list = []
for i in list:
    if i > 0:
        positive_list.append(i)
    else:
        negative_list.append(i)
print("positive numbers list", positive_list)
print("negative numbers list", negative_list)