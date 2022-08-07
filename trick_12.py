# Find the max number using reduce
from functools import reduce

numbers = [1, 34, 2, 1, 4, 5, 2, 1, 32, 1, 4]
max_number = reduce(lambda r, i: r if r > i else i, numbers, 0)
print(max_number)
