"""
Given an array of integers, return all posible indices of the two numbers such that they add up to a specific target.
"""
class Solutions():
    def twosum(self, nums: list, target: int) -> list:
        h = {}
        out = []
        for i, num in enumerate(nums):
            if target - num not in h:
                h[num] = i
                # print(h)
            else:
                out.append((h[target-num], i))
        return out


s = Solutions()
print(s.twosum([0, 1, 2, 3, 5, 9, 22, 21, 20], 22))
