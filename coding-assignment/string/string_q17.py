'''Write a program to reverse each word in a given string while maintaining the order of the words.'''
s = "Hello World"
reversed_words = ""
word = ""
for char in s:
    if char != ' ':
        word = char + word
    else:
        reversed_words += word + " "
        word = ""
reversed_words += word  # Add the last word
print(reversed_words)  # Output: "olleH dlroW"
