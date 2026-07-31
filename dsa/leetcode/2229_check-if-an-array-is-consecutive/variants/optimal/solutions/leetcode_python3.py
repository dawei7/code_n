from typing import List


class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        distinct = set(nums)
        return len(distinct) == len(nums) and max(nums) - min(nums) == len(nums) - 1
