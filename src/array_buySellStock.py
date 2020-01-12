"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""

import time
from nose.tools import assert_equal

# algo : Brute Force
class Solution1:
    def maxProfit(self, prices: list) -> int:
        out = 0
        start_time = time.perf_counter_ns()
        for i in range(len(prices)-1):
            if out < max(prices[i+1:]) - prices[i]:
                out = max(prices[i+1:]) - prices[i]
        return out, str(time.perf_counter_ns() - start_time) + "ns"


# algo : one pass
class Solution2:

    def maxProfit(self, prices:list) -> int:
        start_time = time.perf_counter_ns()
        l = len(prices)
        if not l:
            return 0
        minprice, i, out = prices[0], 0, 0

        for price in prices:
            if price < minprice and i != l-1:
                minprice, iminprice, maxprice = price, i, price
            else:
                maxprice, imaxprice = price, i
            if out < maxprice - minprice:
                out = maxprice - minprice
            i += 1
        return out, str(time.perf_counter_ns() - start_time) + "ns"


s = Solution1()
assert_equal(s.maxProfit([2,1,2,0,1])[0], 1)
assert_equal(s.maxProfit([2, 4, 1])[0], 2)
assert_equal(s.maxProfit([7, 1, 5, 3, 6, 4])[0], 5)
assert_equal(s.maxProfit([7, 6, 5, 4, 3, 2, 1])[0], 0)
assert_equal(s.maxProfit([1, 2])[0], 1)
assert_equal(s.maxProfit([2, 1])[0], 0)
print("algo 1 test passed")
s = Solution2()
assert_equal(s.maxProfit([2,1,2,0,1])[0], 1)
assert_equal(s.maxProfit([2, 4, 1])[0], 2)
assert_equal(s.maxProfit([7, 1, 5, 3, 6, 4])[0], 5)
assert_equal(s.maxProfit([7, 6, 5, 4, 3, 2, 1])[0], 0)
assert_equal(s.maxProfit([1, 2])[0], 1)
assert_equal(s.maxProfit([2, 1])[0], 0)
print("algo 2 test passed")
