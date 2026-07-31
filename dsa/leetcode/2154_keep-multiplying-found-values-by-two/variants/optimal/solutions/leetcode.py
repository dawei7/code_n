from typing import List


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        values = set(nums)
        while original in values:
            original *= 2
        return original
