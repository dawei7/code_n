from typing import List


class Solution:
    def countElements(self, nums: List[int]) -> int:
        minimum = min(nums)
        maximum = max(nums)
        return sum(minimum < value < maximum for value in nums)
