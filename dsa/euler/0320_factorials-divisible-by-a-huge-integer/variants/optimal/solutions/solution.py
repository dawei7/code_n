"""Project Euler 320: Factorials Divisible by a Huge Integer

Find S(1000000) mod 10^18, where S(u) = sum_{i=10}^u N(i)
and N(i) is the smallest integer n such that n! is divisible by (i!)^1234567890.
"""

from __future__ import annotations

import math


def solve(
    upper_limit: int = 1_000_000,
    exponent_multiplier: int = 1_234_567_890,
    mod: int = 1_000_000_000_000_000_000,
) -> str:
    """Calculates S(upper_limit) mod mod using Kempner/Smarandache base-p digit weight decomposition

    and incremental prime factor updates: N(i+1) = max(N(i), max_{p | (i+1)} f(p, M * e_p(i+1))).
    """
    # 1. Precompute Smallest Prime Factor (SPF) for fast linear-time prime factorization
    spf = list(range(upper_limit + 1))
    for i in range(2, int(math.isqrt(upper_limit)) + 1):
        if spf[i] == i:
            for j in range(i * i, upper_limit + 1, i):
                if spf[j] == j:
                    spf[j] = i

    # Function to find min n such that nu_p(n!) >= E using base-p weight decomposition
    def get_min_n(p: int, req_e: int) -> int:
        if req_e == 0:
            return 0
        w = 1
        p_pow = 1
        weights: list[tuple[int, int]] = []
        while w <= req_e:
            weights.append((w, p_pow))
            w = w * p + 1
            p_pow *= p

        res_n = 0
        rem = req_e
        for weight, p_val in reversed(weights):
            digit = rem // weight
            rem %= weight
            res_n += digit * (p_val * p)
        if rem > 0:
            res_n += p
        return res_n

    # Prime exponents e_p in i!
    e_p = [0] * (upper_limit + 1)

    # Pre-accumulate prime exponents for i in [2, 9]
    for i in range(2, 10):
        temp = i
        while temp > 1:
            p = spf[temp]
            cnt = 0
            while temp % p == 0:
                cnt += 1
                temp //= p
            e_p[p] += cnt

    cur_n = 0
    for p in range(2, 10):
        if e_p[p] > 0:
            req_val = get_min_n(p, exponent_multiplier * e_p[p])
            if req_val > cur_n:
                cur_n = req_val

    total_s = 0

    # Incrementally update prime factor contributions for i = 10 .. upper_limit
    for i in range(10, upper_limit + 1):
        temp = i
        while temp > 1:
            p = spf[temp]
            cnt = 0
            while temp % p == 0:
                cnt += 1
                temp //= p
            e_p[p] += cnt
            req_val = get_min_n(p, exponent_multiplier * e_p[p])
            if req_val > cur_n:
                cur_n = req_val

        total_s = (total_s + cur_n) % mod

    return str(total_s)


if __name__ == "__main__":
    print(solve())
