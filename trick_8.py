# Flatten nested list and get odd numbers squared
regular_list = [[1, 2, 3, 4], [5, 6, 7], [8, 9]]
flat_list = [item ** 2 for sub_list in regular_list for item in sub_list if item % 2 != 0]
print(flat_list)
