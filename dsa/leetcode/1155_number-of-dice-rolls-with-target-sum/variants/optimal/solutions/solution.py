class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        modulus = 1_000_000_007
        if target < n or target > n * k:
            return 0

        dp = [0] * (target + 1)
        dp[0] = 1
        for _ in range(n):
            next_dp = [0] * (target + 1)
            window = 0
            for total in range(1, target + 1):
                window += dp[total - 1]
                if total - k - 1 >= 0:
                    window -= dp[total - k - 1]
                next_dp[total] = window % modulus
            dp = next_dp
        return dp[target]
