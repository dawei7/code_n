"""Project Euler Problem 521: Smallest Prime Factor.

Find S(10^12) mod 10^9, where S(n) is the sum of the smallest prime factor
smpf(i) for all integers 2 <= i <= n.
"""

from math import isqrt
from typing import List

MOD = 1_000_000_000


def _initial_sum(x: int) -> int:
    if x < 2:
        return 0
    return (x * (x + 1) // 2 - 1) % MOD


def solve(n: int = 10**12, mod: int = MOD) -> int:
    """Compute S(n) mod mod using sublinear Lucy / Min_25 smallest prime factor sieve."""
    if n < 2:
        return 0

    root = isqrt(n)

    count_small: List[int] = [0] * (root + 1)
    sum_small: List[int] = [0] * (root + 1)
    for x in range(1, root + 1):
        count_small[x] = x - 1
        sum_small[x] = _initial_sum(x)

    count_large: List[int] = [0] * (root + 1)
    sum_large: List[int] = [0] * (root + 1)
    for d in range(1, root + 1):
        x = n // d
        count_large[d] = x - 1
        sum_large[d] = _initial_sum(x)

    answer = 0

    for p in range(2, root + 1):
        count_before = count_small[p - 1]
        if count_small[p] == count_before:
            continue

        sum_before = sum_small[p - 1]
        answer = (
            answer + p * ((count_large[p] - count_before) % mod)
        ) % mod

        p2 = p * p
        large_stop = n // p2
        if large_stop > root:
            large_stop = root

        for d in range(1, large_stop + 1):
            q = n // (d * p)
            if q <= root:
                q_count = count_small[q]
                q_sum = sum_small[q]
            else:
                idx = n // q
                q_count = count_large[idx]
                q_sum = sum_large[idx]

            count_large[d] -= q_count - count_before
            sum_large[d] = (
                sum_large[d] - p * ((q_sum - sum_before) % mod)
            ) % mod

        if p2 <= root:
            for x in range(root, p2 - 1, -1):
                q = x // p
                count_small[x] -= count_small[q] - count_before
                sum_small[x] = (
                    sum_small[x] - p * ((sum_small[q] - sum_before) % mod)
                ) % mod

    return (answer + sum_large[1]) % mod


if __name__ == "__main__":
    print(solve())
