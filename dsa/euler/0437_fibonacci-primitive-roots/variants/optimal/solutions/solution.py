"""Project Euler Problem 437: Fibonacci Primitive Roots.

Find the sum of all primes less than 100_000_000 that have at least one Fibonacci primitive root.
"""

from math import isqrt
from typing import Iterator, List


def _is_prime_mr32(n: int) -> bool:
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n == p:
            return True
        if n % p == 0:
            return False

    d = n - 1
    s = 0
    while (d & 1) == 0:
        d >>= 1
        s += 1

    for a in (2, 3, 5, 7, 11):
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True


def _tonelli_shanks(n: int, p: int) -> int:
    n %= p
    if n == 0:
        return 0
    if p % 4 == 3:
        return pow(n, (p + 1) // 4, p)

    q = p - 1
    s = 0
    while (q & 1) == 0:
        q >>= 1
        s += 1

    z = 2
    while pow(z, (p - 1) // 2, p) != p - 1:
        z += 1

    c = pow(z, q, p)
    r = pow(n, (q + 1) // 2, p)
    t = pow(n, q, p)
    m = s

    while t != 1:
        i = 1
        t2i = (t * t) % p
        while t2i != 1:
            t2i = (t2i * t2i) % p
            i += 1
        b = pow(c, 1 << (m - i - 1), p)
        rb = (r * b) % p
        bb = (b * b) % p
        t = (t * bb) % p
        c = bb
        r = rb
        m = i

    return r


def _is_primitive_root(
    g: int, p: int, prime_factors_p_minus_1: List[int]
) -> bool:
    pm1 = p - 1
    for q in prime_factors_p_minus_1:
        if pow(g, pm1 // q, p) == 1:
            return False
    return True


def _simple_sieve(limit: int) -> List[int]:
    if limit < 2:
        return []
    if limit == 2:
        return [2]
    size = (limit // 2) + 1
    sieve = bytearray(b"\x01") * size
    sieve[0] = 0
    r = isqrt(limit)
    for odd in range(3, r + 1, 2):
        if sieve[odd // 2]:
            start = (odd * odd) // 2
            step = odd
            count = ((size - 1 - start) // step) + 1
            sieve[start::step] = b"\x00" * count
    primes = [2]
    primes.extend(2 * i + 1 for i in range(1, size) if sieve[i])
    return primes


def _iter_primes_below(
    n: int, base_primes: List[int], segment_odd_count: int = 1 << 20
) -> Iterator[int]:
    if n <= 2:
        return
    yield 2
    span = 2 * segment_odd_count
    low = 3
    while low < n:
        high = min(low + span, n)
        seg_len = (high - low + 1) // 2
        seg = bytearray(b"\x01") * seg_len

        for p in base_primes[1:]:
            pp = p * p
            if pp >= high:
                break
            start = pp if pp >= low else ((low + p - 1) // p) * p
            if (start & 1) == 0:
                start += p
            idx = (start - low) // 2
            step = p
            if idx < seg_len:
                count = ((seg_len - 1 - idx) // step) + 1
                seg[idx::step] = b"\x00" * count

        i = seg.find(1)
        while i != -1:
            yield low + 2 * i
            i = seg.find(1, i + 1)

        low = high if (high & 1) else (high + 1)


def _distinct_prime_factors(
    n: int, primes_up_to_1e4: List[int], idx_after_97: int
) -> List[int]:
    factors: List[int] = []
    if (n & 1) == 0:
        factors.append(2)
        while (n & 1) == 0:
            n //= 2
    if n == 1:
        return factors

    for p in primes_up_to_1e4[1:idx_after_97]:
        if p * p > n:
            break
        if n % p == 0:
            factors.append(p)
            while n % p == 0:
                n //= p
            if n == 1:
                return factors

    if n > 97 * 97 and _is_prime_mr32(n):
        factors.append(n)
        return factors

    for p in primes_up_to_1e4[idx_after_97:]:
        if p * p > n:
            break
        if n % p == 0:
            factors.append(p)
            while n % p == 0:
                n //= p
            if n == 1:
                return factors
            if n > p * p and _is_prime_mr32(n):
                factors.append(n)
                return factors

    if n > 1:
        factors.append(n)
    return factors


def _has_fib_primitive_root(
    p: int, primes_up_to_1e4: List[int], idx_after_97: int
) -> bool:
    if p == 5:
        return True
    if p % 5 not in (1, 4):
        return False

    if p % 4 == 3:
        s = pow(5, (p + 1) // 4, p)
    else:
        s = _tonelli_shanks(5, p)

    inv2 = (p + 1) // 2
    g1 = ((1 + s) * inv2) % p
    g2 = ((1 - s) * inv2) % p

    factors = _distinct_prime_factors(p - 1, primes_up_to_1e4, idx_after_97)

    if _is_primitive_root(g1, p, factors):
        return True
    if _is_primitive_root(g2, p, factors):
        return True
    return False


def solve(limit_exclusive: int = 100_000_000) -> int:
    """Compute the sum of primes < limit_exclusive with at least one Fibonacci primitive root."""
    if limit_exclusive <= 2:
        return 0

    base_limit = isqrt(limit_exclusive - 1) + 1
    base_primes = _simple_sieve(base_limit)
    primes_1e4 = (
        base_primes if base_limit >= 10_000 else _simple_sieve(10_000)
    )

    idx_after_97 = 0
    while idx_after_97 < len(primes_1e4) and primes_1e4[idx_after_97] <= 97:
        idx_after_97 += 1

    total = 0
    if 5 < limit_exclusive:
        total += 5

    for p in _iter_primes_below(limit_exclusive, base_primes):
        if p == 2 or p == 5:
            continue
        if p % 5 not in (1, 4):
            continue
        if _has_fib_primitive_root(p, primes_1e4, idx_after_97):
            total += p

    return total


if __name__ == "__main__":
    print(solve())
