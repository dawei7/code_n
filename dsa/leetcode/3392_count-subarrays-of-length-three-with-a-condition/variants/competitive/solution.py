from typing import List


class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count = 0
        for index in range(len(nums) - 2):
            if 2 * (nums[index] + nums[index + 2]) == nums[index + 1]:
                count += 1
        return count
