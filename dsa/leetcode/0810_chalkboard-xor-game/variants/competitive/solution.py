from typing import List


class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        total_xor = 0
        for value in nums:
            total_xor ^= value
        return total_xor == 0 or len(nums) % 2 == 0
