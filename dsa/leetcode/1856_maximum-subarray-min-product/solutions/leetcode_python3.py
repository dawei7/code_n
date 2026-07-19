from itertools import accumulate
from typing import List


class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        prefix = list(accumulate(nums, initial=0))
        stack = []
        best = 0

        for right, value in enumerate(nums):
            left = right
            while stack and stack[-1][1] >= value:
                start, minimum = stack.pop()
                best = max(best, minimum * (prefix[right] - prefix[start]))
                left = start
            stack.append((left, value))

        for left, minimum in stack:
            best = max(best, minimum * (prefix[len(nums)] - prefix[left]))

        return best % 1_000_000_007
