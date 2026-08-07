from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        values = set(nums)
        return max((value for value in values if value > 0 and -value in values), default=-1)
