"""Optimal app-local solution for LeetCode 1039."""


def solve(values):
    vertex_count = len(values)
    dp = [[0] * vertex_count for _ in range(vertex_count)]

    for length in range(3, vertex_count + 1):
        for left in range(vertex_count - length + 1):
            right = left + length - 1
            dp[left][right] = min(
                dp[left][middle]
                + dp[middle][right]
                + values[left] * values[middle] * values[right]
                for middle in range(left + 1, right)
            )

    return dp[0][vertex_count - 1]
