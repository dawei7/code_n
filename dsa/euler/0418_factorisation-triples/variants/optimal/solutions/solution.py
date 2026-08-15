"""Project Euler Problem 418: Factorisation Triples.

Find f(43!), where f(n) is the sum a+b+c for the unique triple 1 <= a <= b <= c, a*b*c = n
minimising c/a.
"""

from bisect import bisect_left, bisect_right
from math import exp, log
from typing import List, Optional, Tuple


def _prime_sieve(limit: int) -> List[int]:
    if limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    r = int(limit**0.5)
    for p in range(2, r + 1):
        if sieve[p]:
            step = p
            start = p * p
            sieve[start : limit + 1 : step] = b"\x00" * (
                ((limit - start) // step) + 1
            )
    return [i for i in range(2, limit + 1) if sieve[i]]


def _legendre_factorial_exponent(n: int, p: int) -> int:
    s = 0
    while n:
        n //= p
        s += n
    return s


def _generate_divisors(primes: List[int], exps: List[int]) -> List[int]:
    divs = [1]
    for p, e in zip(primes, exps):
        pe = 1
        new: List[int] = []
        for _ in range(e + 1):
            for d in divs:
                new.append(d * pe)
            pe *= p
        divs = new
    return divs


def _choose_split(exps: List[int], max_divisors: int) -> int:
    dcount = 1
    split = 0
    for i, e in enumerate(exps):
        if i > 0 and dcount * (e + 1) > max_divisors:
            break
        dcount *= e + 1
        split = i + 1
    return split


def _divisors_in_range(
    l_bound: int, h_bound: int, divs1_sorted: List[int], divs2: List[int]
) -> List[int]:
    if l_bound > h_bound:
        return []
    res: List[int] = []
    for d2 in divs2:
        lo = (l_bound + d2 - 1) // d2
        hi = h_bound // d2
        if lo > hi:
            continue
        i = bisect_left(divs1_sorted, lo)
        j = bisect_right(divs1_sorted, hi)
        for d1 in divs1_sorted[i:j]:
            res.append(d1 * d2)
    return res


def _best_triple_from_candidates(
    n: int, a_list: List[int], c_list: List[int]
) -> Optional[Tuple[int, int, int]]:
    best: Optional[Tuple[int, int, int]] = None
    c_sorted = sorted(c_list)
    for a in a_list:
        for c in c_sorted:
            if c < a:
                continue
            ac = a * c
            if n % ac != 0:
                continue
            b = n // ac
            if a <= b <= c:
                if best is None:
                    best = (a, b, c)
                else:
                    if c * best[0] < best[2] * a:
                        best = (a, b, c)
    return best


def solve(k_val: int = 43) -> int:
    """Find f(k_val!) using meet-in-the-middle divisor range search near the cube root."""
    primes = _prime_sieve(k_val)
    exps = [_legendre_factorial_exponent(k_val, p) for p in primes]

    split = _choose_split(exps, max_divisors=1_000_000)
    p1, e1 = primes[:split], exps[:split]
    p2, e2 = primes[split:], exps[split:]

    divs1 = _generate_divisors(p1, e1)
    divs1.sort()
    divs2 = _generate_divisors(p2, e2) if p2 else [1]

    # Compute n = k! dynamically
    n = 1
    for i in range(2, k_val + 1):
        n *= i

    cbrt = exp(log(n) / 3.0)

    delta = 1e-6
    while delta <= 0.05:
        a_l = max(1, int(cbrt / (1.0 + delta)) - 2)
        a_h = int(cbrt) + 2
        c_l = max(1, int(cbrt) - 2)
        c_h = int(cbrt * (1.0 + delta)) + 2

        a_list = _divisors_in_range(a_l, a_h, divs1, divs2)
        c_list = _divisors_in_range(c_l, c_h, divs1, divs2)

        if a_list and c_list:
            if len(a_list) * len(c_list) <= 50_000_000:
                best = _best_triple_from_candidates(n, a_list, c_list)
                if best is not None:
                    a, b, c = best
                    return a + b + c

        delta *= 2.0

    raise RuntimeError("Failed to find factorisation triple.")


if __name__ == "__main__":
    print(solve())
