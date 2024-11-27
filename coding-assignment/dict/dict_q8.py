'''Write a program create a dictionary from two lists, one containing keys and the other containing values.'''
# Lists of keys and values
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'New York']

# Creating the dictionary
dict_from_lists = dict(zip(keys, values))

# Printing the dictionary
print("Dictionary from lists:", dict_from_lists)
