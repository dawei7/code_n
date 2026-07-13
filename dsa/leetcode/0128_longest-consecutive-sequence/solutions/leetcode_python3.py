from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        values = set(nums)
        best = 0
        for value in values:
            if value - 1 in values:
                continue
            current = value
            while current in values:
                current += 1
            best = max(best, current - value)
        return best
