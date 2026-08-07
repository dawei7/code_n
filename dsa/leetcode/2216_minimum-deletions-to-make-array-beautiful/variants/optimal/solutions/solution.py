from typing import List


class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        deletions = 0
        for index in range(len(nums) - 1):
            if (index - deletions) % 2 == 0 and nums[index] == nums[index + 1]:
                deletions += 1
        if (len(nums) - deletions) % 2:
            deletions += 1
        return deletions
