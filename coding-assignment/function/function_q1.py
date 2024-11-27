'''Write a function to find the factorial of a number.'''
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
