from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        suffix_values = set()
        for index in range(len(nums) - 1, -1, -1):
            if nums[index] in suffix_values:
                return index // 3 + 1
            suffix_values.add(nums[index])
        return 0
