from typing import List


class Solution:
    def subsequenceCount(self, nums: List[int]) -> int:
        if not any(value % 2 for value in nums):
            return 0
        return pow(2, len(nums) - 1, 1_000_000_007)
