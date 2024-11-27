'''Write a program combine two tuples element-wise into a list of tuples.'''
# Creating two tuples
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')

# Zipping tuples
zipped = list(zip(tuple1, tuple2))

# Printing the zipped list
print("Zipped list:", zipped)
