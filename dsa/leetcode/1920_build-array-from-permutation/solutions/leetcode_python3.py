from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[value] for value in nums]
