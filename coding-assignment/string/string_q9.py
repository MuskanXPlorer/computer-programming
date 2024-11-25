'''Write a function to check if two strings are anagrams (i.e., they contain the same characters in different order).'''
#Taking input from user for two string
str1 = input()
str2 = input()
l =len(str1)
c = 0
#logic section
for i in str1:
    for j in str2:
        if i==j:
            c=c+1
#check the string
if c==l:
    print("anagram")
else:
    print("not anagrams")
