'''Write a function to check if a number is a perfect number.'''
def is_perfect_number(n: int) -> bool:
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

n = int(input("Enter a number to check if it's perfect: "))
if is_perfect_number(n):
    print(f"{n} is a perfect number.")
else:
    print(f"{n} is not a perfect number.")
