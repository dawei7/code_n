"""Project Euler 271: Modular Cubes, Part 1

Find S(13082761331670030), the sum of all integers 1 < x < n such that x^3 = 1 mod n.
"""

from __future__ import annotations

import itertools


def solve(n: int = 13082761331670030) -> str:
    """Calculates S(n) by finding all cube roots of unity modulo each prime factor of n

    and combining them via the Chinese Remainder Theorem (CRT).
    """
    # Factor square-free n into prime factors
    primes: list[int] = []
    temp = n
    d = 2
    while d * d <= temp:
        if temp % d == 0:
            primes.append(d)
            while temp % d == 0:
                temp //= d
        d += 1
    if temp > 1:
        primes.append(temp)

    # For each prime factor p, find all solutions to r^3 = 1 mod p
    roots_by_p: list[list[int]] = []
    crt_weights: list[int] = []

    for p in primes:
        roots = [r for r in range(1, p) if (r * r * r) % p == 1]
        roots_by_p.append(roots)

        # Precompute CRT weight: M_i * (M_i^-1 mod p_i)
        m_i = n // p
        y_i = pow(m_i, -1, p)
        crt_weights.append(m_i * y_i)

    # Combine all root combinations via Chinese Remainder Theorem
    total_sum = 0
    for choice in itertools.product(*roots_by_p):
        x = sum(r * w for r, w in zip(choice, crt_weights)) % n
        if x > 1:
            total_sum += x

    return str(total_sum)


if __name__ == "__main__":
    print(solve())
