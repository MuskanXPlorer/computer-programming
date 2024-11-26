'''Write a program to find the Longest Word in a String and smallest word'''
#input of string from user
string1 = input("enter the string: ")
word = string1.split()
largest = word[0]
small = word[0]
#finding the longest and smallest word in a given string
for i in range(len(word)):
  if len(largest) < len(word[i]):
    largest = word[i]
  elif len(small) > len (word[i]):
    small = word[i]
#display section
print("largest word is ",largest)
print("smallest word is ",small)
