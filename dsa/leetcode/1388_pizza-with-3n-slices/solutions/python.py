"""Optimal solution for LeetCode 1388: Pizza With 3n Slices."""


def solve(slices: list[int]) -> int:
    choose = len(slices) // 3

    def best_linear(values: list[int]) -> int:
        dp = [[0] * (choose + 1) for _ in range(len(values) + 2)]
        for i, value in enumerate(values, start=2):
            for count in range(1, choose + 1):
                dp[i][count] = max(dp[i - 1][count], dp[i - 2][count - 1] + value)
        return dp[-1][choose]

    return max(best_linear(slices[:-1]), best_linear(slices[1:]))
