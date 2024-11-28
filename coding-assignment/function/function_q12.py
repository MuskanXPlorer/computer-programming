'''Write a function to calculate the power of a number using a loop.'''
def power(base: int, exponent: int) -> int:
    result = 1
    for _ in range(exponent):
        result *= base
    return result

base = int(input
