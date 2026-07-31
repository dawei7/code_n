from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        counts = {}
        window_sum = 0
        best = 0

        for right, value in enumerate(nums):
            counts[value] = counts.get(value, 0) + 1
            window_sum += value

            if right >= k:
                outgoing = nums[right - k]
                window_sum -= outgoing
                counts[outgoing] -= 1
                if counts[outgoing] == 0:
                    del counts[outgoing]

            if right >= k - 1 and len(counts) == k:
                best = max(best, window_sum)

        return best
