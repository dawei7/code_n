from typing import List


class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        base = 0
        best_gain = 0
        greatest_lower = float("-inf")
        least_upper = float("inf")

        for index in range(1, len(nums)):
            left = nums[index - 1]
            right = nums[index]
            edge = abs(left - right)
            base += edge
            best_gain = max(best_gain, abs(nums[0] - right) - edge)
            best_gain = max(best_gain, abs(nums[-1] - left) - edge)
            greatest_lower = max(greatest_lower, min(left, right))
            least_upper = min(least_upper, max(left, right))

        best_gain = max(best_gain, 2 * (greatest_lower - least_upper))
        return base + best_gain
