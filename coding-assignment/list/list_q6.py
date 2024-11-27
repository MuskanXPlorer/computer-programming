'''Write a Python program to remove multiple elements from a list based on the given condition.'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Elements to remove
to_remove = [3, 5, 7]

# Removing elements
for item in to_remove:
    if item in numbers:
        numbers.remove(item)

# Output the modified list
print(numbers)
