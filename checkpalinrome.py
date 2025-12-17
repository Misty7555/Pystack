s = input("Enter a string: ")
rev = ""
i = 0
length = 0
for ch in s:
    length += 1
i = length - 1
while i >= 0:
    rev = rev + s[i]
    i -= 1
if s == rev:
    print("Palindrome")
else:
    print("Not a Palindrome")