"""Project Euler Problem 478: Mixtures.

Find E(10_000_000) mod 11^8, the number of subsets of primitive mixtures M(n)
that can produce the mixture ratio (1 : 1 : 1).
"""

from typing import List, Tuple

MOD = 11**8


def _sieve_phi_and_mu(n: int) -> Tuple[List[int], List[int]]:
    phi = list(range(n + 1))
    mu = [0] * (n + 1)
    mu[1] = 1
    primes: List[int] = []
    is_prime = [True] * (n + 1)

    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
            mu[i] = -1
            phi[i] = i - 1
        for p in primes:
            if i * p > n:
                break
            is_prime[i * p] = False
            if i % p == 0:
                phi[i * p] = phi[i] * p
                mu[i * p] = 0
                break
            else:
                phi[i * p] = phi[i] * (p - 1)
                mu[i * p] = -mu[i]

    return phi, mu


def solve(n: int = 10_000_000, mod: int = MOD) -> int:
    """Compute E(n) mod mod using hexagonal projective ray multiplicity and Dirichlet summation."""
    phi, mu = _sieve_phi_and_mu(n)
    m = [0] * (n + 1)

    for s in range(1, n + 1):
        cnt = n - s + 1
        j1 = n // s
        if j1 >= 2:
            cnt += (j1 - 1) * n - s * (j1 * (j1 + 1) // 2 - 1)
        m[s] = cnt

    for d in range(2, n + 1):
        md = mu[d]
        if md == 0:
            continue
        nd = n // d
        max_s = nd
        if md == 1:
            for s in range(1, max_s + 1):
                j = nd // s
                m[s] += j * nd - s * (j * (j + 1) // 2)
        else:
            for s in range(1, max_s + 1):
                j = nd // s
                m[s] -= j * nd - s * (j * (j + 1) // 2)

    n0 = sum(6 * phi[s] * m[s] for s in range(1, n + 1))
    inv2 = (mod + 1) // 2
    sum_val = 0

    for s in range(1, n + 1):
        term = 6 * phi[s] * (1 - pow(inv2, m[s], mod)) % mod
        sum_val = (sum_val + term) % mod

    bad = pow(2, n0 // 2, mod) * sum_val % mod
    return (pow(2, n0 + 1, mod) - 1 - bad) % mod


if __name__ == "__main__":
    print(solve())
