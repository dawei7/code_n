from typing import List


class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        ordered = sorted(nums)
        smaller_levels = 0
        operations = 0

        for index in range(1, len(ordered)):
            if ordered[index] != ordered[index - 1]:
                smaller_levels += 1
            operations += smaller_levels

        return operations
