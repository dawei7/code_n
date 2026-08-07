from collections import defaultdict
from typing import List


class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        positions_by_value = defaultdict(list)
        for index, value in enumerate(nums):
            positions_by_value[value].append(index)

        best = 0
        for positions in positions_by_value.values():
            left = 0
            for right in range(len(positions)):
                while positions[right] - positions[left] - (right - left) > k:
                    left += 1
                best = max(best, right - left + 1)

        return best
