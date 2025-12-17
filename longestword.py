sentence = input("Enter a sentence: ")
longest = ""
word = ""
for ch in sentence:
    if ch != " ":
        word = word + ch
    else:
        if len(word) > len(longest):
            longest = word
        word = ""
if len(word) > len(longest):
    longest = word
print("longest word: ", longest)