'''Write a function that checks if a number is a happy number.'''
def is_happy_number(n: int) -> bool:
    def get_sum_of_squares(num: int) -> int:
        return sum(int(i) ** 2 for i in str(num))
    
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_sum_of_squares(n)
    return n == 1

n = int(input("Enter a number to check if it's a happy number: "))
if is_happy_number(n):
    print(f"{n} is a happy number.")
else:
    print(f"{n} is not a happy number.")
