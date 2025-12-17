string = input("Enter a sentence: ")
max_count = 0 
max_char = ''
for i in range(len(string)):
    count = 0
    for j in range (len(string)):
        if string[i] == string[j]:
            count = count + 1
    if count > max_count:
        max_count = count
        max_char = string[i]
print("Most frequent character: ", max_char)