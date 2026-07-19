from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix = 0
        minimum_prefix = 0
        for value in nums:
            prefix += value
            minimum_prefix = min(minimum_prefix, prefix)
        return 1 - minimum_prefix
