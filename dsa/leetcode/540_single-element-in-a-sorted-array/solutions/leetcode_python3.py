from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lower = 0
        upper = len(nums) - 1
        while lower < upper:
            middle = (lower + upper) // 2
            if middle % 2:
                middle -= 1
            if nums[middle] == nums[middle + 1]:
                lower = middle + 2
            else:
                upper = middle
        return nums[lower]
