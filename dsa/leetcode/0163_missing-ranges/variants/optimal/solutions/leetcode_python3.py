from typing import List


class Solution:
    def findMissingRanges(
        self, nums: List[int], lower: int, upper: int
    ) -> List[List[int]]:
        ranges = []
        next_missing = lower
        for value in nums:
            if next_missing < value:
                ranges.append([next_missing, value - 1])
            next_missing = value + 1
        if next_missing <= upper:
            ranges.append([next_missing, upper])
        return ranges
