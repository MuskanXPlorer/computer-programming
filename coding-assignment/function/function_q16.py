'''Write a function to calculate the sum of even numbers in a list.'''
def sum_of_even_numbers(lst: list) -> int:
    return sum(num for num in lst if num % 2 == 0)

lst = list(map(int, input("Enter a list of numbers: ").split()))
print(f"The sum of even numbers in the list is {sum_of_even_numbers(lst)}")
