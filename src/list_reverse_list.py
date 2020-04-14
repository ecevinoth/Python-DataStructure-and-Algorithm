# Different ways to reverse a list

input_data = [1, 3, 5, 7, 9]
# expected output [9, 7, 5, 3, 1]

# method 1: use range with negative step value
print(input_data[::-1])

# method 2: reversed function
print(list(reversed(input_data)))

# method 3: inplace reverse
input_data.reverse() # wont return anything
print(input_data)

# method 4: using list comprehension
print([input_data[num] for num in range(len(input_data)-1, -1, -1)])
