from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        up = 1
        down = 1
        for index in range(1, len(nums)):
            if nums[index] > nums[index - 1]:
                up = down + 1
            elif nums[index] < nums[index - 1]:
                down = up + 1
        return max(up, down)

