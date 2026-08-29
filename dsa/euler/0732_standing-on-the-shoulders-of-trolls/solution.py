"""Project Euler Problem 732: Standing on the Shoulders of Trolls.

Find Q(1000), the maximum total IQ of escaping trolls from a hole of depth
D_N = (1 / sqrt(2)) * sum_{n=0}^{N-1} h_n.
"""

import math
from typing import List, Tuple

_MOD = 1_000_000_007


def _generate_trolls(n: int) -> List[Tuple[int, int, int]]:
    total_r = 3 * n
    r = [0] * total_r
    p = 1
    for i in range(total_r):
        r[i] = (p % 101) + 50
        p = (p * 5) % _MOD

    trolls = []
    for k in range(n):
        h = r[3 * k]
        l = r[3 * k + 1]
        q = r[3 * k + 2]
        trolls.append((h, l, q))
    return trolls


def solve(n: int = 1000) -> int:
    """Compute Q(n) using deadline-constrained 0/1 knapsack dynamic programming on sorted jobs."""
    trolls = _generate_trolls(n)
    total_h = sum(h for h, _, _ in trolls)

    a = total_h * total_h
    y = math.isqrt((a - 1) // 2) + 1
    base = total_h - y

    jobs: List[Tuple[int, int, int]] = []
    max_d = 0
    for h, l, q in trolls:
        d = base + l + h
        if h <= d:
            jobs.append((d, h, q))
            if d > max_d:
                max_d = d

    # Earliest Deadline First (EDF) order
    jobs.sort()

    dp = [-1] * (max_d + 1)
    dp[0] = 0

    for d, p, profit in jobs:
        for t in range(d, p - 1, -1):
            prev = dp[t - p]
            if prev != -1:
                cand = prev + profit
                if cand > dp[t]:
                    dp[t] = cand

    ans = max(dp)
    return ans


if __name__ == "__main__":
    print(solve())
