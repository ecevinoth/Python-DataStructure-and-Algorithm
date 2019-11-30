def csum(n):
    # base case 
    if n == 0:
        return 0
    else:
        return n + csum(n-1)

print("enter an integer?")
print(csum(int(input())))
