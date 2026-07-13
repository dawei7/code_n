from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        median = nums[len(nums) // 2]
        total = 0
        for value in nums:
            total += abs(value - median)
        return total
