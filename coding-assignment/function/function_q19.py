'''Write a function that takes a list of strings and returns the longest string.'''
def longest_string(lst: list) -> str:
    longest = lst[0]
    for string in lst:
        if len(string) > len(longest):
            longest = string
    return longest

lst = input("Enter a list of strings separated by space: ").split()
print(f"The longest string is '{longest_string(lst)}'")
