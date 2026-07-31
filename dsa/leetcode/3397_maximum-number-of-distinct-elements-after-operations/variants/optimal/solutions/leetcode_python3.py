from typing import List


class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        previous = -10**30
        distinct = 0

        for value in nums:
            assigned = max(value - k, previous + 1)
            if assigned <= value + k:
                previous = assigned
                distinct += 1

        return distinct
