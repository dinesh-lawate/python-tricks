# Get sum,mul of n numbers of input
from functools import reduce


def sum_of_numbers(*numbers):
    result = 0
    for number in numbers:
        result += number

    return result


def sum_of_numbers_reduce(*numbers):
    return reduce(lambda s, i: s + i, numbers, 0)


def mul_of_numbers_reduce(*numbers):
    return reduce(lambda m, i: m * i, numbers, 1)


print(sum_of_numbers(1, 2, 3, 4, 5))
print(sum_of_numbers_reduce(1, 2, 3, 4, 5))
print(mul_of_numbers_reduce(1, 2, 3, 4, 5))
