from typing import List


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        operation_count = len(multipliers)
        scores = [0] * (operation_count + 1)

        for operation in range(operation_count - 1, -1, -1):
            multiplier = multipliers[operation]
            for left_taken in range(operation + 1):
                right_index = len(nums) - 1 - (operation - left_taken)
                take_left = multiplier * nums[left_taken] + scores[left_taken + 1]
                take_right = multiplier * nums[right_index] + scores[left_taken]
                scores[left_taken] = max(take_left, take_right)

        return scores[0]
