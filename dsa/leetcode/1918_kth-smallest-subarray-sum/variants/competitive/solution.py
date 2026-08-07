from typing import List


class Solution:
    def kthSmallestSubarraySum(self, nums: List[int], k: int) -> int:
        def count_at_most(limit: int) -> int:
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

        low = min(nums)
        high = sum(nums)
        while low < high:
            middle = (low + high) // 2
            if count_at_most(middle) >= k:
                high = middle
            else:
                low = middle + 1

        return low
