'''Write a program to Multiply All Numbers in the List in Python.'''
a = [2, 4, 8, 3]

# Initialize result variable to 1
res = 1

# Loop through each value in list
for val in a:
  
    # Multiply current result by the current value
    res = res * val
    
print(res)
