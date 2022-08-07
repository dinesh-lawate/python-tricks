# Get most repeated number from below list of numbers
a = [1, 1, 1, 1, 1, 2, 3, 1, 3, 4, 2, 1, 2, 4, 3, 2, 1, 5, 7, 5, 3, 2, 1, 2, 4, 5, 53, 1, 2, 34, 2, 1, 2, 3, 5, 3, 2, 1,
     2, 3]
print(a)
most_repeated_number = max(set(a), key=a.count)
print(most_repeated_number)
