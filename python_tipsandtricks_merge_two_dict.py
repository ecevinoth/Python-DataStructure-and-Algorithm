# given input parameter
x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}

# python 3.5+
# using (**) operator - unpack dictionary elements
z = {**x, **y}
print(z)
# {'c': 4, 'a': 1, 'b': 3}

# python 2.x
# use this:
z = dict(x, **y)
print(z)
{'a': 1, 'c': 4, 'b': 3}
