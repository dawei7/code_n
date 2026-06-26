"""Optimal solution for LeetCode 1039: Minimum Score Triangulation of Polygon."""


def solve(values: list[int]) -> int:
    n = len(values)
    dp = [[0] * n for _ in range(n)]
    for length in range(3, n + 1):
        for left in range(n - length + 1):
            right = left + length - 1
            dp[left][right] = min(
                dp[left][mid]
                + dp[mid][right]
                + values[left] * values[mid] * values[right]
                for mid in range(left + 1, right)
            )
    return dp[0][n - 1]
