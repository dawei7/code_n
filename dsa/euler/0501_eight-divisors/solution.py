"""Project Euler Problem 501: Eight Divisors.

Find f(10^12), the count of numbers not exceeding 10^12 with exactly eight divisors.
"""

from bisect import bisect_right
from math import isqrt
from typing import List


def _iroot(n: int, k: int) -> int:
    if n < 2:
        return n
    r = int(round(n ** (1.0 / k)))
    while (r + 1) ** k <= n:
        r += 1
    while r**k > n:
        r -= 1
    return r


def _sieve_primes(limit: int) -> List[int]:
    if limit < 2:
        return []
    flags = bytearray(b"\x01") * (limit + 1)
    flags[0:2] = b"\x00\x00"
    for p in range(2, isqrt(limit) + 1):
        if flags[p]:
            start = p * p
            flags[start : limit + 1 : p] = b"\x00" * (
                ((limit - start) // p) + 1
            )
    return [i for i in range(2, limit + 1) if flags[i]]


def solve(limit: int = 10**12) -> int:
    """Compute f(limit) using sublinear prime counting sieve (Lucy's algorithm) and divisor structure decomposition."""
    if limit < 24:
        return 0

    root = isqrt(limit)
    primes = _sieve_primes(root)

    small = [0] * (root + 1)
    for x in range(2, root + 1):
        small[x] = x - 1
    large = [0] * (root + 1)
    for d in range(1, root + 1):
        large[d] = limit // d - 1

    for p in primes:
        p2 = p * p
        if p2 > limit:
            break
        before_p = small[p - 1]

        last_d = min(root, limit // p2)
        for d in range(1, last_d + 1):
            pd = p * d
            if pd <= root:
                large[d] -= large[pd] - before_p
            else:
                large[d] -= small[limit // pd] - before_p

        for x in range(root, p2 - 1, -1):
            small[x] -= small[x // p] - before_p

    def pi_fn(x: int) -> int:
        if x < 2:
            return 0
        if x <= root:
            return small[x]
        return large[limit // x]

    count = 0

    # Pattern 1: p * q * r (p < q < r)
    p_stop = bisect_right(primes, _iroot(limit, 3))
    for i in range(p_stop):
        p = primes[i]
        if p * p * p >= limit:
            break
        q_stop = bisect_right(primes, isqrt(limit // p))
        for j in range(i + 1, q_stop):
            q = primes[j]
            max_r = limit // (p * q)
            if max_r <= q:
                break
            count += pi_fn(max_r) - (j + 1)

    # Pattern 2: p^3 * q (p != q)
    for p in primes[:p_stop]:
        p3 = p * p * p
        if p3 > limit:
            break
        count += pi_fn(limit // p3)
    count -= pi_fn(_iroot(limit, 4))

    # Pattern 3: p^7
    count += pi_fn(_iroot(limit, 7))

    return count


if __name__ == "__main__":
    print(solve())
