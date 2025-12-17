s = input("Enter a string: ")
result = ""
for ch in s:
    found = False
    for r in result:
        if ch == r:
            found = True
            break
    if not found:
        result = result + ch
print("String after removing duplicates:", result)
