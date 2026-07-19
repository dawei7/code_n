from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = nums[0]
        current_max = best_max = nums[0]
        current_min = best_min = nums[0]

        for value in nums[1:]:
            current_max = max(value, current_max + value)
            best_max = max(best_max, current_max)
            current_min = min(value, current_min + value)
            best_min = min(best_min, current_min)
            total += value

        if best_max < 0:
            return best_max
        return max(best_max, total - best_min)

