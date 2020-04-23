# Implementation of Brian Kernighan’s Algorithm
# Function to get no of set bits in binary
# time complexity of this approach is : O(log n)


def count_set_bits(n):
    count = 0               # Initialize count: = 0
    while n:                # if n is not zero
        # Do "bitwise AND" with (n-1) and assign the value back to n
        n &= (n - 1)
        count += 1          # increment count by 1
    return count            # return final count


print("assert checking started")
assert count_set_bits(9) == str(bin(9)).count('1')
assert count_set_bits(100) == str(bin(100)).count('1')
assert count_set_bits(1) == str(bin(1)).count('1')
print("all condition passed")
