
def count_ones(n):
    count = 0

    while (n):
        count += n & 1
        print(count, n)
        n >>= 1
    return count



i=13
print(count_ones(i))