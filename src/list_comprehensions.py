"""
list comprehension are awesome.

vales = [expression for value in collection if condition]

# equivalent
vals = []
for value in collection:
    if condition:
        vals.append(expression)
"""

even_square = [x * x for x in range(10) if not x % 2]
print(even_square)
