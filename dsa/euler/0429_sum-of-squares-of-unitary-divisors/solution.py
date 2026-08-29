"""Project Euler Problem 429: Sum of Squares of Unitary Divisors.

Find S(100_000_000!) mod 1_000_000_009, where S(n) is the sum of squares of unitary divisors of n.
"""

from math import isqrt

MOD = 1_000_000_009


def solve(n_val: int = 100_000_000) -> int:
    """Compute S(n_val!) mod MOD using Legendre's formula and multiplicative product over primes."""
    size = (n_val + 1) // 2
    sieve = bytearray(b"\x01") * size
    sieve[0] = 0
    r = isqrt(n_val)
    for i in range(1, (r // 2) + 1):
        if sieve[i]:
            p = 2 * i + 1
            start = (p * p) // 2
            sieve[start::p] = b"\x00" * (((size - start - 1) // p) + 1)

    ans = 1

    # Prime 2
    e = 0
    m = n_val
    while m > 0:
        m //= 2
        e += m
    ans = (ans * (1 + pow(2, 2 * e, MOD))) % MOD

    # Odd primes
    idx = sieve.find(1, 1)
    while idx != -1:
        p = 2 * idx + 1
        e = 0
        m = n_val
        while m > 0:
            m //= p
            e += m
        ans = (ans * (1 + pow(p, 2 * e, MOD))) % MOD
        idx = sieve.find(1, idx + 1)

    return ans


if __name__ == "__main__":
    print(solve())
