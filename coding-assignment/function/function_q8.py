'''Write a function to find the second largest element in a list.'''
def second_largest(lst):
    first, second = float('-inf'), float('-inf')
    for num in lst:
        if num > first:
            first, second = num, first
        elif first > num > second:
            second = num
    return second
