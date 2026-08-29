"""Project Euler Problem 634: Numbers of the Form a^2 b^3.

Find F(9 * 10^18), where F(n) is the number of integers x <= n of the form x = a^2 b^3 (a, b >= 2).
"""

import math
from typing import List, Tuple


def _sieve_mu(limit: int) -> Tuple[List[int], List[int]]:
    mu = [0] * (limit + 1)
    mu[1] = 1
    primes: List[int] = []
    is_p = [True] * (limit + 1)
    is_p[0] = is_p[1] = False

    for i in range(2, limit + 1):
        if is_p[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            if i * p > limit:
                break
            is_p[i * p] = False
            if i % p == 0:
                mu[i * p] = 0
                break
            mu[i * p] = -mu[i]

    return mu, primes


def solve(n: int = 9 * 10**18) -> int:
    """Compute F(N) using squarefree kernel separation and cubefree inclusion-exclusion."""
    # Term 1: x = a^2 b^3 with b >= 2 squarefree, a >= 2
    b_max = int((n / 4) ** (1 / 3)) + 5
    mu_b, _ = _sieve_mu(b_max)

    term1 = 0
    for b in range(2, b_max + 1):
        if mu_b[b] != 0:
            b3 = b**3
            if b3 * 4 > n:
                break
            max_a = int(math.isqrt(n // b3))
            if max_a >= 2:
                term1 += max_a - 1

    # Term 2: x = (a c^3)^2 with a >= 2, c >= 2 (integers A <= sqrt(n) with composite cube factors)
    k_val = int(math.isqrt(n))
    j_max = int(k_val ** (1 / 3)) + 5
    mu_j, primes_j = _sieve_mu(j_max)

    cubefree_k = 0
    for j in range(1, j_max + 1):
        j3 = j**3
        if j3 > k_val:
            break
        cubefree_k += mu_j[j] * (k_val // j3)

    k_third = int(k_val ** (1 / 3))
    while (k_third + 1) ** 3 <= k_val:
        k_third += 1
    while k_third**3 > k_val:
        k_third -= 1

    pi_k_third = sum(1 for p in primes_j if p <= k_third)
    term2 = k_val - cubefree_k - pi_k_third

    return term1 + term2


if __name__ == "__main__":
    print(solve())
