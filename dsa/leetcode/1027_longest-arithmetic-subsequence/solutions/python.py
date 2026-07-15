"""Optimal app-local solution for LeetCode 1027."""


def solve(nums):
    dp = [{} for _ in nums]
    best = 2

    for i, value in enumerate(nums):
        for j in range(i):
            difference = value - nums[j]
            candidate = dp[j].get(difference, 1) + 1
            dp[i][difference] = max(dp[i].get(difference, 0), candidate)
            best = max(best, dp[i][difference])

    return best
