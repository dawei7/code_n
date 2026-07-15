from typing import List


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0] * (len(arr) + 1)

        for end in range(1, len(arr) + 1):
            current_max = 0
            for length in range(1, min(k, end) + 1):
                current_max = max(current_max, arr[end - length])
                dp[end] = max(
                    dp[end],
                    dp[end - length] + current_max * length,
                )

        return dp[-1]

