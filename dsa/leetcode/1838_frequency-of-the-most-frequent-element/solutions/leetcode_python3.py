from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        window_sum = 0
        best = 1

        for right, target in enumerate(nums):
            window_sum += target
            while target * (right - left + 1) - window_sum > k:
                window_sum -= nums[left]
                left += 1
            best = max(best, right - left + 1)

        return best
