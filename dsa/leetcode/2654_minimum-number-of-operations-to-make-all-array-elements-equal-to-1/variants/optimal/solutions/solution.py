from math import gcd
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ones = nums.count(1)
        if ones:
            return n - ones

        shortest = n + 1
        for left in range(n):
            subarray_gcd = 0
            for right in range(left, n):
                subarray_gcd = gcd(subarray_gcd, nums[right])
                if subarray_gcd == 1:
                    shortest = min(shortest, right - left + 1)
                    break

        if shortest == n + 1:
            return -1
        return shortest - 1 + n - 1
