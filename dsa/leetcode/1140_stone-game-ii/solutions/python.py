from functools import lru_cache


def solve(piles):
    n = len(piles)
    suffix = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        suffix[i] = suffix[i + 1] + piles[i]

    @lru_cache(None)
    def dp(i, m):
        if i + 2 * m >= n:
            return suffix[i]
        best_opponent = float("inf")
        for x in range(1, 2 * m + 1):
            best_opponent = min(best_opponent, dp(i + x, max(m, x)))
        return suffix[i] - best_opponent

    return dp(0, 1)
