from typing import List


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        candidates = []
        for index, value in enumerate(nums):
            if not candidates or value < nums[candidates[-1]]:
                candidates.append(index)

        maximum = 0
        for right in range(len(nums) - 1, -1, -1):
            while candidates and nums[candidates[-1]] <= nums[right]:
                maximum = max(maximum, right - candidates.pop())
        return maximum
