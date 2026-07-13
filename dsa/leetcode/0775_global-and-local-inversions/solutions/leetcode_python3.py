from typing import List


class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        prefix_maximum = nums[0]
        for right in range(2, len(nums)):
            prefix_maximum = max(prefix_maximum, nums[right - 2])
            if prefix_maximum > nums[right]:
                return False
        return True
