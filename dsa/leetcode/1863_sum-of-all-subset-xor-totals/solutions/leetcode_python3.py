from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        combined_bits = 0
        for value in nums:
            combined_bits |= value
        return combined_bits << (len(nums) - 1)
