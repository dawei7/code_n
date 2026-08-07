from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        ordered = sorted(nums, reverse=True)
        total = sum(ordered)
        selected_sum = 0
        for length, value in enumerate(ordered, start=1):
            selected_sum += value
            if selected_sum > total - selected_sum:
                return ordered[:length]
        return ordered
