from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        first = nums[0]
        for value in nums:
            if value != first:
                return 1
        return 0
