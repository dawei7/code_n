from collections import deque
from typing import List


class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0] * (n + 2)
        candidates = deque()

        for fruit in range(n, 0, -1):
            next_fruit = fruit + 1
            while candidates and dp[candidates[-1]] >= dp[next_fruit]:
                candidates.pop()
            candidates.append(next_fruit)

            right_limit = min(n + 1, 2 * fruit + 1)
            while candidates[0] > right_limit:
                candidates.popleft()

            dp[fruit] = prices[fruit - 1] + dp[candidates[0]]

        return dp[1]
