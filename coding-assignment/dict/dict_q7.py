'''Writa a program create and access elements in a nested dictionary.'''
# Creating a nested dictionary
nested_dict = {
    'person1': {'name': 'Alice', 'age': 25},
    'person2': {'name': 'Bob', 'age': 30}
}

# Accessing nested dictionary elements
name_person1 = nested_dict['person1']['name']

# Printing the value
print("Name of person1:", name_person1)
