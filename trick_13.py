# Merge two dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 4, 'c': 6}

dict3 = {**dict1, **dict2}
print(type(dict3))
print((dict3['a']))
print(dict3.keys())
print(dict3.items())
print(dict3)
