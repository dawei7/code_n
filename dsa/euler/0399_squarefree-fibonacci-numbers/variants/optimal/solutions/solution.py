"""Project Euler Problem 399: Squarefree Fibonacci Numbers.

Find the 100,000,000th squarefree Fibonacci number. Give the answer as its last 16 digits
followed by a comma and scientific notation rounded to 1 digit after the decimal point.
"""

from collections import defaultdict
from math import floor, gcd, log10
import sys
from typing import Dict, List, Tuple

LAST16_MOD = 10**16


def fib_mod(n_val: int, mod: int) -> int:
    """Fast doubling Fibonacci modulo m."""
    a, b = 0, 1
    for bit in range(n_val.bit_length() - 1, -1, -1):
        two_b_minus_a = (2 * b - a) % mod
        c = (a * two_b_minus_a) % mod
        d = (a * a + b * b) % mod
        if (n_val >> bit) & 1:
            a, b = d, (c + d) % mod
        else:
            a, b = c, d
    return a


def _primes_upto(n_val: int) -> List[int]:
    if n_val < 2:
        return []
    sieve = bytearray([1]) * (n_val + 1)
    sieve[0:2] = b"\x00\x00"
    limit = int(n_val**0.5)
    for i in range(2, limit + 1):
        if sieve[i]:
            sieve[i * i : n_val + 1 : i] = b"\x00" * (
                ((n_val - i * i) // i) + 1
            )
    return [i for i in range(2, n_val + 1) if sieve[i]]


def _unique_prime_factors(n_val: int, small_primes: List[int]) -> List[int]:
    factors: List[int] = []
    x = n_val
    for p in small_primes:
        if p * p > x:
            break
        if x % p == 0:
            factors.append(p)
            while x % p == 0:
                x //= p
    if x > 1:
        factors.append(x)
    return factors


def _rank_of_apparition(p: int, small_primes: List[int]) -> int:
    if p == 2:
        return 3
    if p == 5:
        return 5
    legendre = 1 if pow(5, (p - 1) // 2, p) == 1 else -1
    cand = p - 1 if legendre == 1 else p + 1
    d = cand
    for q in _unique_prime_factors(cand, small_primes):
        while d % q == 0 and fib_mod(d // q, p) == 0:
            d //= q
    return d


def _prime_bound(nmax: int) -> int:
    a, b = 0, 1
    best = 0
    for k in range(1, 200):
        a, b = b, a + b
        best = max(best, min(a, nmax // k))
        if k > 60 and (nmax // k) <= best:
            break
    return best


def solve(target_k: int = 100_000_000) -> str:
    """Find the target_k-th squarefree Fibonacci number via rank-of-apparition inclusion-exclusion."""
    nmax = 200_000_000
    pmax = _prime_bound(nmax)
    primes = _primes_upto(pmax)
    small_primes = _primes_upto(int((pmax + 1) ** 0.5) + 1)

    mods: List[int] = []
    for p in primes:
        zp = _rank_of_apparition(p, small_primes)
        m = p * zp
        if m <= nmax:
            mods.append(m)

    mods.sort()

    # Filter redundant multiples
    filtered_mods: List[int] = []
    for m in mods:
        if not any(m % k == 0 for k in filtered_mods):
            filtered_mods.append(m)

    # Inclusion-exclusion coefficients
    sys.setrecursionlimit(10000)
    coeff: Dict[int, int] = defaultdict(int)
    coeff[1] = 1
    l_len = len(filtered_mods)

    def dfs(start: int, lcm_val: int, sign: int) -> None:
        for i in range(start, l_len):
            m = filtered_mods[i]
            if lcm_val % m == 0:
                continue
            nl = (lcm_val // gcd(lcm_val, m)) * m
            if nl > nmax:
                continue
            s = -sign
            coeff[nl] += s
            dfs(i + 1, nl, s)

    dfs(0, 1, 1)

    items = sorted(coeff.items())
    lcms = [k for k, _ in items]
    coeffs = [v for _, v in items]

    def count_sqfree(n: int) -> int:
        return sum(c * (n // l) for l, c in zip(lcms, coeffs))

    # Binary search for the target_k-th index
    lo, hi = 1, nmax
    while lo < hi:
        mid = (lo + hi) // 2
        if count_sqfree(mid) >= target_k:
            hi = mid
        else:
            lo = mid + 1

    ans_n = lo

    # Last 16 digits
    last16 = fib_mod(ans_n, LAST16_MOD)

    # Scientific notation: F_n approx phi^n / sqrt(5)
    phi = (1.0 + 5.0**0.5) / 2.0
    log10_f = ans_n * log10(phi) - 0.5 * log10(5.0)

    exponent = int(floor(log10_f))
    mantissa = 10.0 ** (log10_f - exponent)
    mant_rounded = round(mantissa, 1)
    if mant_rounded >= 10.0:
        mant_rounded = 1.0
        exponent += 1

    return f"{last16:016d},{mant_rounded:.1f}e{exponent}"


if __name__ == "__main__":
    print(solve())
