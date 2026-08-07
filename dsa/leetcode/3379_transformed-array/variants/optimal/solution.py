from typing import List


class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        length = len(nums)
        return [nums[(index + offset) % length] for index, offset in enumerate(nums)]
