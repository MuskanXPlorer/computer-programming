'''Write a program to check if element exists in python.'''
a = [10, 20, 30, 40, 50]

# Check if 30 exists in the list using a loop
key = 30
flag = False

for val in a:
    if val == key:
        flag = True
        break

if flag:
    print("Element exists in the list")
else:
    print("Element does not exist")'''


