from typing import List


class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        nums.sort()
        groups = len(nums) // 3
        return sum(nums[groups::2])
