from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        ordered = sorted(nums)
        return sum(ordered[::2])

