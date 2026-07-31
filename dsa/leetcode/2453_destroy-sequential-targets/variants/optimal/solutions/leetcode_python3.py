from collections import Counter
from typing import List


class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        remainder_counts = Counter(value % space for value in nums)
        return min(nums, key=lambda value: (-remainder_counts[value % space], value))
