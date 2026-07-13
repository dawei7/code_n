from typing import List


class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        advantage = nums.copy()
        for length in range(2, len(nums) + 1):
            for left in range(len(nums) - length + 1):
                right = left + length - 1
                take_left = nums[left] - advantage[left + 1]
                take_right = nums[right] - advantage[left]
                advantage[left] = max(take_left, take_right)
        return advantage[0] >= 0
