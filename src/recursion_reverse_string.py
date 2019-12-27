"""
Topic : recursion - reverse a string without using slicing s[::-1] or iteration
Date : 2019/12/27
Author : ecevinoth
"""
from nose.tools import assert_equal

def reverse(s):
    if len(s) <= 1:
        return s
    else:
        m = int(len(s)/2)
        return reverse(s[m:]) + reverse(s[:m])

class TestReverse():
    def test_rev(self, solution):
        assert_equal(solution("Hello"), "olleH")
        assert_equal(solution("123456789"), "987654321")
        print("all test passed.")
test = TestReverse()
test.test_rev(reverse)