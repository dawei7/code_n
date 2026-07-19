from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operations = 0
        previous = nums[0]
        for value in nums[1:]:
            adjusted = max(value, previous + 1)
            operations += adjusted - value
            previous = adjusted
        return operations
