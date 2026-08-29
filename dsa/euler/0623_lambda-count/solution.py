"""Project Euler Problem 623: Lambda Count.

Mathematical Formulation:
Count closed lambda terms of size <= 2000 modulo 1000000007.
"""

from __future__ import annotations


def solve(n_max: int = 2000, mod: int = 1000000007) -> str:
    """Compute closed lambda terms count mod (10^9+7)."""
    # DP over term sizes (size, number of free variables)
    dp = [0] * (n_max + 1)
    dp[1] = 1  # variable
    for size in range(2, n_max + 1):
        # Application: sum_{i=1}^{size-2} dp[i] * dp[size-1-i]
        app_count = sum(dp[i] * dp[size - 1 - i] for i in range(1, size - 1)) % mod
        # Abstraction: dp[size - 1]
        abs_count = dp[size - 1]
        dp[size] = (app_count + abs_count) % mod

    total = sum(dp[1 : n_max + 1]) % mod
    return str(total)


if __name__ == "__main__":
    print(solve())
