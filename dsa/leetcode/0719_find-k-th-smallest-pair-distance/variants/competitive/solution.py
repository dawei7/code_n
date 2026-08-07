from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        low = 0
        high = nums[-1] - nums[0]

        while low < high:
            middle = (low + high) // 2
            count = 0
            left = 0

            for right, value in enumerate(nums):
                while value - nums[left] > middle:
                    left += 1
                count += right - left

            if count >= k:
                high = middle
            else:
                low = middle + 1

        return low
