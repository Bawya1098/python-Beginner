from collections import Counter

dict1 = {'a': 100, 'b': 100, 'c': 100, 'd': 100}
dict2 = {'a': 200, 'b': 200, 'c': 200, 'd': 200}

dict3 = Counter(dict1) + Counter(dict2)

print(dict3)
