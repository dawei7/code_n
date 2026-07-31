from typing import List


class Solution:
    def sumOfPower(self, nums: List[int], k: int) -> int:
        mod = 1_000_000_007
        dp = [0] * (k + 1)
        dp[0] = 1

        for value in nums:
            next_dp = [ways * 2 % mod for ways in dp]
            if value <= k:
                for total in range(value, k + 1):
                    next_dp[total] = (next_dp[total] + dp[total - value]) % mod
            dp = next_dp

        return dp[k]
