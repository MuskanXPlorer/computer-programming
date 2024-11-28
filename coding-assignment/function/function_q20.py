'''Write a function to find the nth triangular number.'''
def triangular_number(n: int) -> int:
    return n * (n + 1) // 2

n = int(input("Enter a number to find the nth triangular number: "))
print(f"The {n}th triangular number is {triangular_number(n)}")
