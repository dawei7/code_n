from typing import List


class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        limit = nums[-1]
        operations = 0
        for value in reversed(nums[:-1]):
            pieces = (value + limit - 1) // limit
            operations += pieces - 1
            limit = value // pieces
        return operations
