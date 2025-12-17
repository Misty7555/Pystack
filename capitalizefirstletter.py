sentence = input("Enter a sentence: ")
result = ""
capitalize_next = True 
for ch in sentence:
    if ch == " ":
        result += ch
        capitalize_next = True
    elif capitalize_next:
        result += ch.capitalize()  
        capitalize_next = False
    else:
        result += ch
print("Capitalized sentence:", result)
