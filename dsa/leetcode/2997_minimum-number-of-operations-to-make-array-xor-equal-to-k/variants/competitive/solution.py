from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        difference = k
        for value in nums:
            difference ^= value
        return difference.bit_count()
