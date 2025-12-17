s = input("Enter a string: ")
vowels = 0
consonants = 0
digits = 0
alphabets = 0
for ch in s:
    if ch >= '0' and ch <= '9':
        digits += 1
    elif (ch >= 'A' and ch <= 'Z') or (ch >= 'a' and ch <= 'z'):
        alphabets += 1
        if ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U' or \
           ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
            vowels += 1
        else:
            consonants += 1
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Alphabets:", alphabets)
