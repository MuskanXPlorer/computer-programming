'''Write a program to merge two strings by alternating characters from each string.'''
s1 = "abc"
s2 = "123"
merged = ""
for i in range(max(len(s1), len(s2))):
    if i < len(s1):
        merged += s1[i]
    if i < len(s2):
        merged += s2[i]
print(merged)  # Output: "a1b2c3"
