from typing import List


class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        total_xor = 0
        has_nonzero = False

        for value in nums:
            total_xor ^= value
            if value != 0:
                has_nonzero = True

        if not has_nonzero:
            return 0
        if total_xor != 0:
            return len(nums)
        return len(nums) - 1
