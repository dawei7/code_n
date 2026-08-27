from typing import List


class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for c, t in zip(cost, time):
            vol = t + 1
            for j in range(n, -1, -1):
                prev = max(0, j - vol)
                if dp[prev] + c < dp[j]:
                    dp[j] = dp[prev] + c
        return int(dp[n])
