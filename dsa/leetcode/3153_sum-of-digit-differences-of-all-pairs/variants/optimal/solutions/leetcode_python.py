from typing import List


class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        positions = len(str(nums[0]))
        counts = [[0] * 10 for _ in range(positions)]
        total = 0
        for seen, value in enumerate(nums):
            for position in range(positions):
                digit = value % 10
                total += seen - counts[position][digit]
                counts[position][digit] += 1
                value //= 10
        return total
