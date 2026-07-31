from math import gcd


class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefix_gcd: list[int] = []
        maximum = 0

        for value in nums:
            maximum = max(maximum, value)
            prefix_gcd.append(gcd(value, maximum))

        prefix_gcd.sort()

        total = 0
        left = 0
        right = len(prefix_gcd) - 1
        while left < right:
            total += gcd(prefix_gcd[left], prefix_gcd[right])
            left += 1
            right -= 1

        return total
