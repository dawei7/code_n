"""Project Euler Problem 519: Tricoloured Coin Fountains.

Find the last 9 digits of T(20000), where T(n) is the total number of proper
3-colourings over all valid fountains with n coins.
"""

import math
from typing import List

MOD = 1_000_000_000


def solve(n: int = 20000) -> str:
    """Compute the last 9 digits of T(n) using Dyck-path boundary-height rolling DP."""
    if n <= 0:
        raise ValueError("n must be positive")
    if n == 1:
        return f"{3:09d}"

    max_h = math.isqrt(2 * n) + 2
    buf = max_h + 3
    dp: List[List[int]] = [[0] * (max_h + 2) for _ in range(buf)]

    dp[1 % buf][1] = 3

    for s in range(1, n):
        row = dp[s % buf]
        maxj = min(max_h, math.isqrt(2 * s) + 1)

        suff = [0] * (maxj + 3)
        running = 0
        for h in range(maxj, 0, -1):
            running = (running + row[h]) % MOD
            suff[h] = running

        remaining = n - s
        if remaining <= 0 or running == 0:
            for h in range(1, maxj + 1):
                row[h] = 0
            continue

        dp[(s + 1) % buf][1] = (dp[(s + 1) % buf][1] + 2 * suff[1]) % MOD

        if remaining >= 2:
            dp[(s + 2) % buf][2] = (
                dp[(s + 2) % buf][2] + suff[1] + row[1]
            ) % MOD

        maxk = min(max_h, maxj + 1, remaining)
        for k in range(3, maxk + 1):
            dp[(s + k) % buf][k] = (dp[(s + k) % buf][k] + suff[k - 1]) % MOD

        for h in range(1, maxj + 1):
            row[h] = 0

    limit = math.isqrt(2 * n)
    ans_row = dp[n % buf]
    ans = sum(ans_row[1 : limit + 1]) % MOD
    return f"{ans:09d}"


if __name__ == "__main__":
    print(solve())
