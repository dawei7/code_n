from typing import List


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        for first in range(len(nums) - 2):
            left = first + 1
            right = len(nums) - 1
            while left < right:
                if nums[first] + nums[left] + nums[right] < target:
                    count += right - left
                    left += 1
                else:
                    right -= 1
        return count
