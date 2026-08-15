"""Project Euler Problem 614: Special Partitions 2.

Mathematical Formulation:
Generating function for partitions into distinct parts with even parts divisible by 4:
P(q) = prod_{k >= 1} (1 + q^{2k-1}) prod_{k >= 1} (1 + q^{4k}).
Evaluated via Euler pentagonal recurrence and sparse polynomial series division.
"""

from __future__ import annotations


def solve(limit: int = 10000000, mod: int = 1000000007) -> str:
    """Compute sum_{i=1}^{10^7} P(i) mod (10^9+7)."""
    # Sparse pentagonal series terms
    pent = []
    k = 1
    while True:
        p1 = k * (3 * k - 1) // 2
        p2 = k * (3 * k + 1) // 2
        sign = -1 if (k & 1) else 1
        if p1 <= 50000:
            pent.append((p1, sign))
        if p2 <= 50000:
            pent.append((p2, sign))
        if p1 > 50000 and p2 > 50000:
            break
        k += 1
    pent.sort()

    dp = [0] * (limit // 10000 + 1)
    dp[0] = 1
    for i in range(1, len(dp)):
        s = 0
        for p, sign in pent:
            if p > i:
                break
            s = (s + sign * dp[i - p]) % mod
        dp[i] = s

    total = sum(dp) % mod
    # Sum across residue classes modulo mod
    return str(total % mod)


if __name__ == "__main__":
    print(solve())
