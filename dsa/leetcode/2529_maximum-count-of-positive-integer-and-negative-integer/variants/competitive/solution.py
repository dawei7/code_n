from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        negative = bisect_left(nums, 0)
        positive = len(nums) - bisect_right(nums, 0)
        return max(negative, positive)
