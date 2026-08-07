from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def at_most(limit: int) -> int:
            if limit < 0:
                return 0
            left = 0
            window_sum = 0
            count = 0
            for right, value in enumerate(nums):
                window_sum += value
                while window_sum > limit:
                    window_sum -= nums[left]
                    left += 1
                count += right - left + 1
            return count

        return at_most(goal) - at_most(goal - 1)
