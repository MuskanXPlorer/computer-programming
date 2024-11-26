'''Write  a program to find all permutations of a word'''
s = "abc" 
answer = ""
if len(s) == 0:
  print(answer, end=' ') 
else: 
for i in range(len(s)):
  char = s[i] 
  left_substr = s[0:i]
  right_substr = s[i+1:] 
  rest = left_substr + right_substr 
  for j in range(len(rest) + 1):
    result = rest[:j] + char + rest[j:] 
    print(result, end=' ')
