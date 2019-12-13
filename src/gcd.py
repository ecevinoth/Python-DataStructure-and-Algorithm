"""
find the greast common devisor for the given two numbers
"""
import math

def gcd(d,r):
    if d % r == 0:
        return r
    else:
        return(gcd(r, d % r))

# test case
assert gcd(48, 14) == math.gcd(48, 14)
assert gcd(12, 6) == math.gcd(12, 6)
assert gcd(120, 45) == math.gcd(120, 45)
assert gcd(3000, 123) == math.gcd(3000, 123)

print("GCD program working fine.")
