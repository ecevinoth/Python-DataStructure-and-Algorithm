# How to sort a Python dict by value

dict = {'a': 99, 'b': 0, 'c': 101, 'd': 10, 'e': -1}

print(sorted(dict.items(), key=lambda x: x[1]))

import operator
print(sorted(dict.items(), key=operator.itemgetter(1)))


# [('e', -1), ('b', 0), ('d', 10), ('a', 99), ('c', 101)]
# [('e', -1), ('b', 0), ('d', 10), ('a', 99), ('c', 101)]
