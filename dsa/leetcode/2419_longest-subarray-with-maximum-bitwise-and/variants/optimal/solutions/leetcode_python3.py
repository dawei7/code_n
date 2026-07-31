from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maximum = max(nums)
        longest = 0
        current = 0

        for value in nums:
            if value == maximum:
                current += 1
                longest = max(longest, current)
            else:
                current = 0
        return longest
