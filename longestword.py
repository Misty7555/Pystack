print("Enter a sentence:")
sentence = input()
words = sentence.split()
longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word
print("The longest word is:", longest_word)
