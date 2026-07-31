from math import gcd
from typing import List


class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        mod = 1_000_000_007
        max_value = max(nums)
        dp = [[0] * (max_value + 1) for _ in range(max_value + 1)]
        dp[0][0] = 1

        for value in nums:
            next_dp = [row[:] for row in dp]
            for gcd_first in range(max_value + 1):
                next_first = gcd(gcd_first, value)
                for gcd_second in range(max_value + 1):
                    ways = dp[gcd_first][gcd_second]
                    if ways == 0:
                        continue

                    next_second = gcd(gcd_second, value)
                    next_dp[next_first][gcd_second] = (next_dp[next_first][gcd_second] + ways) % mod
                    next_dp[gcd_first][next_second] = (next_dp[gcd_first][next_second] + ways) % mod
            dp = next_dp

        return sum(dp[g][g] for g in range(1, max_value + 1)) % mod
