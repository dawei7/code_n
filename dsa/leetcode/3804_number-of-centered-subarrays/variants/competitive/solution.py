from typing import List


class Solution:
    def centeredSubarrays(self, nums: List[int]) -> int:
        centered = 0

        for left in range(len(nums)):
            total = 0
            values = set()
            for right in range(left, len(nums)):
                total += nums[right]
                values.add(nums[right])
                if total in values:
                    centered += 1

        return centered
