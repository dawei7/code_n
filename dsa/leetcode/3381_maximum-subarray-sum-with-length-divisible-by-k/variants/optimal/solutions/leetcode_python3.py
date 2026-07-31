from typing import List


class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        minimum_prefix = [float("inf")] * k
        minimum_prefix[0] = 0
        prefix_sum = 0
        answer = float("-inf")

        for length, value in enumerate(nums, 1):
            prefix_sum += value
            remainder = length % k
            answer = max(answer, prefix_sum - minimum_prefix[remainder])
            minimum_prefix[remainder] = min(
                minimum_prefix[remainder], prefix_sum
            )

        return int(answer)
