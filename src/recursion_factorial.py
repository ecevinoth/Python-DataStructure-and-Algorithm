def factorial(n):
    # base case
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print("enter an integer?")
print(factorial(int(input())))
