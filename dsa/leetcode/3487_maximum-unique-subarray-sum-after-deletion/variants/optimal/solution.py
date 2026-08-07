from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        seen_positive = [False] * 101
        positive_sum = 0
        maximum = nums[0]

        for value in nums:
            maximum = max(maximum, value)
            if value > 0 and not seen_positive[value]:
                seen_positive[value] = True
                positive_sum += value

        return positive_sum if positive_sum > 0 else maximum
