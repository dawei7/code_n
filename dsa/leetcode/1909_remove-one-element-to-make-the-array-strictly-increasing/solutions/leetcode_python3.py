from typing import List


class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        removed = False
        previous = nums[0]

        for index in range(1, len(nums)):
            current = nums[index]
            if current > previous:
                previous = current
                continue

            if removed:
                return False
            removed = True

            if index == 1 or current > nums[index - 2]:
                previous = current

        return True
