"""Project Euler 276: Primitive Triangles

Find the number of primitive integer sided triangles (gcd(a, b, c) = 1)
with perimeter not exceeding 10^7.
"""

from __future__ import annotations


def solve(limit: int = 10_000_000) -> str:
    """Calculates the count of primitive integer triangles with perimeter <= limit using Alcuin's formula

    for integer partitions and Dirichlet hyperbola Mobius inversion.
    """
    # 1. Linear sieve for Mobius function mu up to limit
    mu = [0] * (limit + 1)
    mu[1] = 1
    primes: list[int] = []
    is_prime = [True] * (limit + 1)

    for i in range(2, limit + 1):
        if is_prime[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            if i * p > limit:
                break
            is_prime[i * p] = False
            if i % p == 0:
                mu[i * p] = 0
                break
            mu[i * p] = -mu[i]

    # 2. Precompute prefix sum S_T(M) = sum_{k=1}^M T(k)
    s_t = [0] * (limit + 1)
    for p in range(1, limit + 1):
        if p % 2 == 0:
            tp = (p * p + 24) // 48
        else:
            tp = ((p + 3) * (p + 3) + 24) // 48
        s_t[p] = s_t[p - 1] + tp

    # 3. Sum mu(d) * S_T(floor(limit / d)) across all d <= limit
    total_primitive = 0
    for d in range(1, limit + 1):
        if mu[d] != 0:
            total_primitive += mu[d] * s_t[limit // d]

    return str(total_primitive)


if __name__ == "__main__":
    print(solve())
