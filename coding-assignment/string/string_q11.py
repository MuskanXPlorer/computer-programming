'''Write a Python program that reads a list of prices, reverses the digits of each price, and prints the reversed prices.'''
str = input()
item = str.split()
for i in item:
    print(int(i[::-1]),end=" ")
