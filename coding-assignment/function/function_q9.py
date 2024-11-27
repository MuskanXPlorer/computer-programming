'''Create a function that generates all permutations of a given string.'''
def generate_permutations(s):
    # Base case: if the string is empty
    if len(s) == 0:
        return ['']
    
    # Recursive case
    permutations = []
    for i in range(len(s)):
        # Remove the character at index i
        char = s[i]
        # Get the remaining part of the string
        remaining = s[:i] + s[i+1:]
        # Get all permutations of the remaining part of the string
        for perm in generate_permutations(remaining):
            # Add the removed character to the front of each permutation
            permutations.append(char + perm)
    
    return permutations

# Example usage
print(generate_permutations("abc"))
