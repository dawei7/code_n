"""Optimal solution for LeetCode 375: Guess Number Higher or Lower II."""


def solve(n: int) -> int:
    costs = [[0] * (n + 2) for _ in range(n + 2)]

    for length in range(2, n + 1):
        for left in range(1, n - length + 2):
            right = left + length - 1
            best = float("inf")
            for guess in range(left, right + 1):
                candidate = guess + max(
                    costs[left][guess - 1],
                    costs[guess + 1][right],
                )
                best = min(best, candidate)
            costs[left][right] = int(best)

    return costs[1][n]

