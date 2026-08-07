from collections import defaultdict
from typing import List


class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        frequencies = defaultdict(int)
        window_sum = 0
        best_sum = 0

        for right, value in enumerate(nums):
            frequencies[value] += 1
            window_sum += value

            if right >= k:
                outgoing = nums[right - k]
                window_sum -= outgoing
                frequencies[outgoing] -= 1
                if frequencies[outgoing] == 0:
                    del frequencies[outgoing]

            if right >= k - 1 and len(frequencies) >= m:
                best_sum = max(best_sum, window_sum)

        return best_sum
