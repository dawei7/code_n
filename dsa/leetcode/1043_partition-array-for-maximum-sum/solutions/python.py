"""Optimal solution for LeetCode 1043: Partition Array for Maximum Sum."""


def solve(arr: list[int], k: int) -> int:
    dp = [0] * (len(arr) + 1)
    for i in range(1, len(arr) + 1):
        best = 0
        current_max = 0
        for length in range(1, min(k, i) + 1):
            current_max = max(current_max, arr[i - length])
            best = max(best, dp[i - length] + current_max * length)
        dp[i] = best
    return dp[-1]
