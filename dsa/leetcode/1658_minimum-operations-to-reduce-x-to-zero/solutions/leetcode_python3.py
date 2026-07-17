from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        if target < 0:
            return -1

        left = 0
        window_sum = 0
        longest = -1

        for right, value in enumerate(nums):
            window_sum += value
            while window_sum > target and left <= right:
                window_sum -= nums[left]
                left += 1
            if window_sum == target:
                longest = max(longest, right - left + 1)

        return -1 if longest < 0 else len(nums) - longest
