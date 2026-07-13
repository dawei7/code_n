from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []
        for number in nums:
            value = abs(number)
            marker = value - 1
            if nums[marker] < 0:
                duplicates.append(value)
            else:
                nums[marker] = -nums[marker]
        return duplicates
