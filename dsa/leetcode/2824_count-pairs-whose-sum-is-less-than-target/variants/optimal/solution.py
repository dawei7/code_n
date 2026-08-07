from typing import List


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        pairs = 0

        while left < right:
            if nums[left] + nums[right] < target:
                pairs += right - left
                left += 1
            else:
                right -= 1

        return pairs
