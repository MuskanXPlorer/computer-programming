''' Write a function to calculate the Greatest Common Divisor (GCD) of two numbers.'''
def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print(f"The GCD of {a} and {b} is {gcd(a, b)}")
