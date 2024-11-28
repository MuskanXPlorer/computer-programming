'''Write a function that accepts a string and returns a dictionary with the frequency of each character.'''
def char_frequency(s: str) -> dict:
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

s = input("Enter a string to calculate character frequencies: ")
print(f"The character frequencies are: {char_frequency(s)}")
