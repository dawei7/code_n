from typing import List


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        total = 0
        width = max(nums, default=0).bit_length()
        for bit in range(width):
            ones = 0
            for value in nums:
                ones += (value >> bit) & 1
            total += ones * (len(nums) - ones)
        return total
