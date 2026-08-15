"""Project Euler Problem 487: Sums of Power Sums.

Find sum (S_10000(10^12) mod p) over all primes p between 2*10^9 and 2*10^9 + 2000,
where S_k(n) = sum_{i=1..n} f_k(i) and f_k(n) = sum_{j=1..n} j^k.
"""

from math import isqrt
from typing import List


def _is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    for d in range(3, isqrt(n) + 1, 2):
        if n % d == 0:
            return False
    return True


def _lagrange_power_sum(n: int, k: int, p: int) -> int:
    d = k + 1
    y: List[int] = [0] * (d + 1)
    cur = 0
    for j in range(1, d + 1):
        cur = (cur + pow(j, k, p)) % p
        y[j] = cur

    if n <= d:
        return y[n]

    pref = [1] * (d + 1)
    suff = [1] * (d + 1)
    n_mod = n % p

    for j in range(d):
        pref[j + 1] = (pref[j] * (n_mod - j)) % p

    for j in range(d, 0, -1):
        suff[j - 1] = (suff[j] * (n_mod - j)) % p

    fact = [1] * (d + 1)
    for j in range(1, d + 1):
        fact[j] = (fact[j - 1] * j) % p

    invfact = [1] * (d + 1)
    invfact[d] = pow(fact[d], p - 2, p)
    for j in range(d, 0, -1):
        invfact[j - 1] = (invfact[j] * j) % p

    ans = 0
    for j in range(d + 1):
        num = (pref[j] * suff[j]) % p
        den = (invfact[j] * invfact[d - j]) % p
        if (d - j) % 2 == 1:
            den = p - den
        term = (y[j] * num) % p
        term = (term * den) % p
        ans = (ans + term) % p

    return ans


def _s_k_mod_p(n: int, k: int, p: int) -> int:
    fk = _lagrange_power_sum(n, k, p)
    fk1 = _lagrange_power_sum(n, k + 1, p)
    return (((n + 1) % p * fk) - fk1) % p


def solve(
    n: int = 10**12,
    k: int = 10000,
    p_start: int = 2 * 10**9,
    p_end: int = 2 * 10**9 + 2000,
) -> int:
    """Compute sum_{p prime} (S_k(n) mod p) using O(k) Lagrange polynomial interpolation."""
    total_s = 0
    for p in range(p_start, p_end + 1):
        if _is_prime(p):
            total_s += _s_k_mod_p(n, k, p)

    return total_s


if __name__ == "__main__":
    print(solve())
