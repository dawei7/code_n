"""Project Euler 273: Sum of Squares

Find the sum of S(N) for all square-free N only divisible by primes of the form 4k + 1 < 150.
"""

from __future__ import annotations

import math


def solve(max_prime: int = 150) -> str:
    """Calculates the sum of all minimal base representations a for a^2 + b^2 = N across all square-free

    subsets of primes 4k+1 < 150 using Gaussian integer multiplication trees.
    """
    # 1. Extract all primes p = 1 mod 4 < max_prime
    primes: list[int] = []
    for p in range(5, max_prime):
        if p % 4 == 1:
            if all(p % d != 0 for d in range(2, int(p**0.5) + 1)):
                primes.append(p)

    # 2. Factor each prime into irreducible Gaussian integers p = x^2 + y^2 = (x + iy)(x - iy)
    gaussian_primes: list[tuple[int, int]] = []
    for p in primes:
        for x in range(1, int(p**0.5) + 1):
            y2 = p - x * x
            y = math.isqrt(y2)
            if y * y == y2:
                gaussian_primes.append((x, y))
                break

    total_s = 0

    # 3. Recursive generation of all Gaussian integer combinations for all non-empty subsets
    def dfs(idx: int, curr_list: list[tuple[int, int]]) -> None:
        nonlocal total_s
        if curr_list:
            for u, v in curr_list:
                total_s += min(abs(u), abs(v))

        for i in range(idx, len(gaussian_primes)):
            x, y = gaussian_primes[i]
            if not curr_list:
                next_list = [(x, y)]
            else:
                next_list = []
                for u, v in curr_list:
                    next_list.append((u * x - v * y, u * y + v * x))
                    next_list.append((u * x + v * y, v * x - u * y))
            dfs(i + 1, next_list)

    dfs(0, [])

    return str(total_s)


if __name__ == "__main__":
    print(solve())
