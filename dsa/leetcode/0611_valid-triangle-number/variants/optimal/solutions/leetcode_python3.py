from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0

        for largest in range(len(nums) - 1, 1, -1):
            left = 0
            right = largest - 1
            while left < right:
                if nums[left] + nums[right] > nums[largest]:
                    count += right - left
                    right -= 1
                else:
                    left += 1

        return count
