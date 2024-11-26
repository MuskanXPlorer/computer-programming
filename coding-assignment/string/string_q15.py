'''Write a program to remove all vowels from a given string.'''
s = "Hello World"
vowels = "aeiouAEIOU"
result = ""
for char in s:
    if char not in vowels:
        result += char
print(result) 
# Output: "Hll Wrld"
