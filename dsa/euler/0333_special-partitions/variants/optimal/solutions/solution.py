"""Project Euler 333: Special Partitions

Find the sum of all primes q < 1000000 such that P(q) = 1,
where P(n) is the number of partitions of n into 3-smooth numbers (2^i * 3^j)
forming an antichain (no term divides any other term).
"""

from __future__ import annotations

import math


def solve(limit: int = 1_000_000) -> str:
    """Calculates the sum of primes q < limit with P(q) = 1 in pure Python

    using 2D poset antichain DFS branch-and-bound generation.
    """
    # 1. Generate all 3-smooth numbers 2^i * 3^j < limit
    terms: list[tuple[int, int, int]] = []
    i = 0
    while (1 << i) < limit:
        pow2 = 1 << i
        j = 0
        while pow2 * (3**j) < limit:
            terms.append((i, j, pow2 * (3**j)))
            j += 1
        i += 1

    # Pre-organize terms to ensure fast branching
    # (i is strictly increasing, j is strictly decreasing)
    p_counts = [0] * limit

    # Pure Python recursive DFS
    def dfs(last_i: int, last_j: int, current_sum: int) -> None:
        for i2, j2, v in terms:
            if i2 > last_i and j2 < last_j:
                nsum = current_sum + v
                if nsum < limit:
                    p_counts[nsum] += 1
                    dfs(i2, j2, nsum)

    dfs(-1, 100, 0)

    # 2. Sieve prime numbers up to limit
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(math.isqrt(limit)) + 1):
        if is_prime[p]:
            for m in range(p * p, limit, p):
                is_prime[m] = False

    # 3. Sum primes q < limit with P(q) == 1
    total_prime_sum = sum(
        p for p in range(2, limit) if is_prime[p] and p_counts[p] == 1
    )
    return str(total_prime_sum)


if __name__ == "__main__":
    print(solve())
