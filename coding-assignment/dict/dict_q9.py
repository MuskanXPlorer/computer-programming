'''Write a program create a new dictionary containing only items with values greater than 20.'''
# Creating a dictionary
my_dict = {'a': 10, 'b': 25, 'c': 30, 'd': 15}

# Filtering the dictionary
filtered_dict = {k: v for k, v in my_dict.items() if v > 20}

# Printing the filtered dictionary
print("Filtered Dictionary:", filtered_dict)
