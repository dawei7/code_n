from typing import List


class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        size = len(stones)
        if (size - 1) % (k - 1):
            return -1

        prefix = [0]
        for amount in stones:
            prefix.append(prefix[-1] + amount)

        dp = [[0] * size for _ in range(size)]
        for length in range(2, size + 1):
            for left in range(size - length + 1):
                right = left + length - 1
                dp[left][right] = float("inf")
                for middle in range(left, right, k - 1):
                    candidate = dp[left][middle] + dp[middle + 1][right]
                    if candidate < dp[left][right]:
                        dp[left][right] = candidate
                if (length - 1) % (k - 1) == 0:
                    dp[left][right] += prefix[right + 1] - prefix[left]

        return dp[0][size - 1]
