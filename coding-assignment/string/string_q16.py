'''Write a program to rotate a string by a given number of characters to the left.'''
s = "HelloWorld"
n = 3
rotated_string = s[n:] + s[:n]
print(rotated_string) 
# Output: "loWorldHel"
