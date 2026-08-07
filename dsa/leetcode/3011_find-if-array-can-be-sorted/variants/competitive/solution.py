from typing import List


class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        previous_maximum = 0
        index = 0

        while index < len(nums):
            bits = nums[index].bit_count()
            group_minimum = nums[index]
            group_maximum = nums[index]
            index += 1

            while index < len(nums) and nums[index].bit_count() == bits:
                group_minimum = min(group_minimum, nums[index])
                group_maximum = max(group_maximum, nums[index])
                index += 1

            if group_minimum < previous_maximum:
                return False
            previous_maximum = group_maximum

        return True
