from typing import List


class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        maximum = max(nums)
        return k * maximum + k * (k - 1) // 2
