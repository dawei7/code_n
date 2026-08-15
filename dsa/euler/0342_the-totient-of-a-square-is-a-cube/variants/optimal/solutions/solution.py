"""Project Euler 342: The Totient of a Square Is a Cube

Find the sum of all numbers n, 1 < n < 10^10 such that phi(n^2) is a cube.
"""

from __future__ import annotations

import math
import sys

# Increase recursion depth for deep prime search trees
sys.setrecursionlimit(30000)


def solve(limit: int = 10_000_000_000) -> str:
    """Calculates the sum of all integers 1 < n < limit such that phi(n^2) is a perfect cube

    using prime factorization branch-and-bound, p-adic valuation modulo 3 tracking,
    and prime bound p <= sqrt(limit).
    """
    # 1. Sieve primes up to sqrt(limit) = 100,000
    max_p = math.isqrt(limit)
    is_prime = [True] * (max_p + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, math.isqrt(max_p) + 1):
        if is_prime[i]:
            for j in range(i * i, max_p + 1, i):
                is_prime[j] = False
    primes = [i for i in range(2, max_p + 1) if is_prime[i]]

    # 2. Factorize p - 1 for each prime
    p_minus_1_factors: list[list[tuple[int, int]]] = []
    for p in primes:
        temp = p - 1
        f: list[tuple[int, int]] = []
        for q in primes:
            if q * q > temp:
                break
            if temp % q == 0:
                c = 0
                while temp % q == 0:
                    c += 1
                    temp //= q
                f.append((q, c))
        if temp > 1:
            f.append((temp, 1))
        p_minus_1_factors.append(f)

    # 3. Recursive branch-and-bound search from largest prime downwards
    valid_n: set[int] = set()
    exp_map: dict[int, int] = {}

    def dfs(idx: int, current_n: int) -> None:
        if current_n > 1:
            if all(v % 3 == 0 for v in exp_map.values()):
                valid_n.add(current_n)

        if idx < 0:
            return

        p_cur = primes[idx]

        # Prune: if any prime strictly greater than p_cur has exponent != 0 mod 3, it cannot be fixed
        for p, v in exp_map.items():
            if p > p_cur and v % 3 != 0:
                return

        must_include = exp_map.get(p_cur, 0) % 3 != 0

        # Branch 1: Skip p_cur (only legal if p_cur exponent is already 0 mod 3)
        if not must_include:
            dfs(idx - 1, current_n)

        # Branch 2: Include p_cur with exponent e >= 1
        p = p_cur
        p_factors = p_minus_1_factors[idx]
        cur_p_exp = exp_map.get(p, 0) % 3
        req_e_mod3 = (2 * (1 - cur_p_exp)) % 3

        if req_e_mod3 == 0:
            e_candidates = (3, 6, 9)
        elif req_e_mod3 == 1:
            e_candidates = (1, 4, 7)
        else:
            e_candidates = (2, 5, 8)

        p_pow = 1
        for e in range(1, 35):
            p_pow *= p
            if current_n * p_pow >= limit:
                break
            if e in e_candidates:
                # Apply in-place modifications
                for q, c in p_factors:
                    exp_map[q] = exp_map.get(q, 0) + c
                exp_map[p] = exp_map.get(p, 0) + (2 * e - 1)

                dfs(idx - 1, current_n * p_pow)

                # Backtrack
                exp_map[p] -= 2 * e - 1
                if exp_map[p] == 0:
                    del exp_map[p]
                for q, c in p_factors:
                    exp_map[q] -= c
                    if exp_map[q] == 0:
                        del exp_map[q]

    dfs(len(primes) - 1, 1)

    total_sum = sum(valid_n)
    return str(total_sum)


if __name__ == "__main__":
    print(solve())
