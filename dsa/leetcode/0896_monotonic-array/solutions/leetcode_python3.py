from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = True
        decreasing = True

        for previous, current in zip(nums, nums[1:]):
            if previous < current:
                decreasing = False
            elif previous > current:
                increasing = False

            if not increasing and not decreasing:
                return False

        return True
