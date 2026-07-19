import math


def solve(nums: list[int]) -> int:
    mod = 10**9 + 7
    max_value = max(nums)
    dp = [[0] * (max_value + 1) for _ in range(max_value + 1)]
    dp[0][0] = 1

    for value in nums:
        next_dp = [row[:] for row in dp]
        for g1 in range(max_value + 1):
            for g2 in range(max_value + 1):
                count = dp[g1][g2]
                if count == 0:
                    continue

                next_g1 = value if g1 == 0 else math.gcd(g1, value)
                next_g2 = value if g2 == 0 else math.gcd(g2, value)
                next_dp[next_g1][g2] = (next_dp[next_g1][g2] + count) % mod
                next_dp[g1][next_g2] = (next_dp[g1][next_g2] + count) % mod
        dp = next_dp

    return sum(dp[g][g] for g in range(1, max_value + 1)) % mod
