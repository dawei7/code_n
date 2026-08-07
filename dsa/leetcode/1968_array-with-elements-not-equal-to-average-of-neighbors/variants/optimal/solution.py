from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        for index in range(0, len(nums) - 1, 2):
            nums[index], nums[index + 1] = nums[index + 1], nums[index]
        return nums
