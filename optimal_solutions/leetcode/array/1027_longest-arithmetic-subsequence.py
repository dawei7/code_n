"""Optimal solution for LeetCode 1027: Longest Arithmetic Subsequence."""


def solve(nums: list[int]) -> int:
    dp: list[dict[int, int]] = [{} for _ in nums]
    best = 0
    for i, value in enumerate(nums):
        for j in range(i):
            diff = value - nums[j]
            dp[i][diff] = dp[j].get(diff, 1) + 1
            best = max(best, dp[i][diff])
    return best
