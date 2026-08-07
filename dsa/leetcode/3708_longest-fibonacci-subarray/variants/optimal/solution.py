from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        best = 2
        current = 2

        for index in range(2, len(nums)):
            if nums[index] == nums[index - 1] + nums[index - 2]:
                current += 1
                best = max(best, current)
            else:
                current = 2

        return best
