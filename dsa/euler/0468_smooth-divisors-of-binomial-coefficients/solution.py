"""Project Euler Problem 468: Smooth Divisors of Binomial Coefficients.

Find F(11_111_111) mod 1_000_000_993, where F(n) = sum_{B=1..n} sum_{r=0..n} S_B(C(n, r))
and S_B(x) is the largest B-smooth divisor of x.
"""

from typing import List, Tuple

MOD = 1_000_000_993


def _sieve_spf_and_primes(n: int) -> Tuple[List[int], List[int]]:
    spf = [0] * (n + 1)
    primes: List[int] = []
    for i in range(2, n + 1):
        if spf[i] == 0:
            spf[i] = i
            primes.append(i)
            for j in range(i * i, n + 1, i):
                if spf[j] == 0:
                    spf[j] = i
    return spf, primes


def solve(n: int = 11_111_111, mod: int = MOD) -> int:
    """Compute F(n) mod mod using online binomial prime updates and segment tree prefix products."""
    spf, primes = _sieve_spf_and_primes(n)
    m = len(primes)
    prime_index = [-1] * (n + 1)
    for i, p in enumerate(primes):
        prime_index[p] = i

    weights = [0] * m
    for i in range(m - 1):
        weights[i] = primes[i + 1] - primes[i]
    weights[-1] = n - primes[-1] + 1

    base = 1
    while base < m:
        base <<= 1
    prod = [1] * (2 * base)
    segsum = [0] * (2 * base)

    for i in range(m):
        segsum[base + i] = weights[i] % mod

    for i in range(base - 1, 0, -1):
        l = i << 1
        r = l + 1
        prod[i] = (prod[l] * prod[r]) % mod
        segsum[i] = (segsum[l] + prod[l] * segsum[r]) % mod

    inv_primes = [pow(p, mod - 2, mod) for p in primes]

    def mul_leaf(i: int, factor: int) -> None:
        pos = base + i
        new_val = (prod[pos] * factor) % mod
        prod[pos] = new_val
        segsum[pos] = (weights[i] * new_val) % mod
        pos >>= 1
        while pos:
            l = pos << 1
            r = l + 1
            prod[pos] = (prod[l] * prod[r]) % mod
            segsum[pos] = (segsum[l] + prod[l] * segsum[r]) % mod
            pos >>= 1

    mid = n // 2
    total = 0
    n_even = (n & 1) == 0

    for r in range(0, mid + 1):
        h = (1 + segsum[1]) % mod
        if n_even and r == mid:
            total = (total + h) % mod
            break
        else:
            total = (total + 2 * h) % mod

        x = n - r
        while x > 1:
            p = spf[x]
            idx = prime_index[p]
            mul_leaf(idx, p)
            x //= p

        y = r + 1
        while y > 1:
            p = spf[y]
            idx = prime_index[p]
            mul_leaf(idx, inv_primes[idx])
            y //= p

    return total % mod


if __name__ == "__main__":
    print(solve())
