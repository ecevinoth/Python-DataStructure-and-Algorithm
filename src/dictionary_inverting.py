# Inverting a Dictionary using Dictionary comprehension

# how to convert key and values
input_data = {
    "alpha": "a",
    "beta": "b",
    "gamma": "c"
}

print(input_data)

# using dictionary comprehension to achieve our output
output_data = {
    value: key for key, value in input_data.items()
}

print(output_data)
