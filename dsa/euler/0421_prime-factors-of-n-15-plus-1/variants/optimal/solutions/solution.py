"""Project Euler Problem 421: Prime Factors of n^15 + 1.

Find sum_{n=1..10^11} s(n, 10^8), where s(n, m) is the sum of distinct prime factors of n^15+1 <= m.
"""

from math import isqrt
from typing import Iterator

_SMALL_BASES = (
    2,
    3,
    5,
    7,
    11,
    13,
    17,
    19,
    23,
    29,
    31,
    37,
    41,
    43,
    47,
    53,
    59,
    61,
    67,
    71,
    73,
    79,
    83,
    89,
    97,
)


def _iter_odd_primes_upto(limit: int) -> Iterator[int]:
    if limit < 3:
        return
    size = (limit + 1) // 2
    sieve = bytearray(b"\x01") * size
    sieve[0] = 0

    r = isqrt(limit)
    for i in range(1, (r // 2) + 1):
        if sieve[i]:
            p = 2 * i + 1
            start = (p * p) // 2
            sieve[start::p] = b"\x00" * (((size - start - 1) // p) + 1)

    idx = sieve.find(1, 1)
    while idx != -1:
        yield 2 * idx + 1
        idx = sieve.find(1, idx + 1)


def _is_order_15(g: int, p: int) -> bool:
    if g == 1:
        return False
    g2 = (g * g) % p
    g3 = (g2 * g) % p
    if g3 == 1:
        return False
    g4 = (g2 * g2) % p
    g5 = (g4 * g) % p
    if g5 == 1:
        return False
    return True


def _find_generator_of_subgroup(p: int, d: int) -> int:
    exp = (p - 1) // d
    for a in _SMALL_BASES:
        if a >= p:
            break
        g = pow(a, exp, p)
        if d == 3:
            if g != 1:
                return g
        elif d == 5:
            if g != 1:
                return g
        else:
            if _is_order_15(g, p):
                return g

    upper = min(p, 500)
    for a in range(2, upper):
        g = pow(a, exp, p)
        if d == 3:
            if g != 1:
                return g
        elif d == 5:
            if g != 1:
                return g
        else:
            if _is_order_15(g, p):
                return g

    raise RuntimeError(f"Failed to find generator of order {d} for p={p}")


def solve(l_bound: int = 10**11, m_bound: int = 10**8) -> int:
    """Compute sum_{n=1..l_bound} s(n, m_bound) by swapping summation to prime roots mod p."""
    d_table = [1] * 30
    d_table[1] = 15
    d_table[11] = 5
    d_table[7] = d_table[13] = d_table[19] = 3

    ans = 0

    if m_bound >= 2:
        ans += 2 * ((l_bound + 1) // 2)

    for p in _iter_odd_primes_upto(m_bound):
        d = d_table[p % 30]
        q, t = divmod(l_bound, p)

        if d == 1:
            cnt = q + (1 if t == p - 1 else 0)
            ans += p * cnt
            continue

        g = _find_generator_of_subgroup(p, d)

        threshold = p - t
        u = 1
        extra = 0
        for _ in range(d):
            if u >= threshold:
                extra += 1
            u = (u * g) % p

        cnt = d * q + extra
        ans += p * cnt

    return ans


if __name__ == "__main__":
    print(solve())
