from typing import List


class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        score = nums[0] + nums[1]
        operations = 0

        for index in range(0, len(nums) - 1, 2):
            if nums[index] + nums[index + 1] != score:
                break
            operations += 1

        return operations
