def check(s):
    if s == s[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

s = input("Enter string: ")
check(s)
