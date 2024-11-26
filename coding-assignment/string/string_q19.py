'''Write a program to remove leading and trailing spaces from a string without using built-in strip function.'''
s = "  Hello World  "
start = 0
end = len(s) - 1

while start < len(s) and s[start] == ' ':
    start += 1
while end >= 0 and s[end] == ' ':
    end -= 1

trimmed = ""
for i in range(start, end + 1):
    trimmed += s[i]
print(trimmed)  
# Output: "Hello World"
