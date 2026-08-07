from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        prefix = 0
        minimum_prefix = 0
        maximum_prefix = 0

        for value in nums:
            prefix += value
            minimum_prefix = min(minimum_prefix, prefix)
            maximum_prefix = max(maximum_prefix, prefix)

        return maximum_prefix - minimum_prefix
