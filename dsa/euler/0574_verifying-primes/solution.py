"""Project Euler Problem 574: Verifying Primes.

Find S(3800), where S(n) = sum_{prime p < n} V(p), and V(p) is the smallest A
verifying p as prime in p = A + B or p = A - B with gcd(A, B) = 1, rad(AB) >= primorial(q).
"""

import bisect
import math
from typing import Dict, List, Optional, Tuple


def _sieve(limit: int) -> List[int]:
    if limit < 2:
        return []
    is_prime = bytearray(b"\x01") * (limit + 1)
    is_prime[0:2] = b"\x00\x00"
    r = int(math.isqrt(limit))
    for p in range(2, r + 1):
        if is_prime[p]:
            start = p * p
            step = p
            is_prime[start : limit + 1 : step] = b"\x00" * (
                ((limit - start) // step) + 1
            )
    return [i for i in range(2, limit + 1) if is_prime[i]]


def _egcd(a: int, b: int) -> Tuple[int, int, int]:
    if b == 0:
        return a, 1, 0
    g, x1, y1 = _egcd(b, a % b)
    return g, y1, x1 - (a // b) * y1


def _modinv(a: int, m: int) -> int:
    a %= m
    g, x, _ = _egcd(a, m)
    if g != 1:
        raise ValueError("No modular inverse")
    return x % m


class _CRTData:
    __slots__ = ("q", "primes_lt_q", "modulus", "bases")

    def __init__(
        self, q: int, primes_lt_q: List[int], modulus: int, bases: List[int]
    ) -> None:
        self.q = q
        self.primes_lt_q = primes_lt_q
        self.modulus = modulus
        self.bases = bases


def _build_crt_data(primes_for_q: List[int]) -> Dict[int, _CRTData]:
    data: Dict[int, _CRTData] = {}
    for q in primes_for_q:
        p_list = [r for r in primes_for_q if r < q]
        modulus = 1
        for r in p_list:
            modulus *= r
        bases: List[int] = []
        for r in p_list:
            mr = modulus // r
            inv = _modinv(mr % r, r)
            bases.append((mr * inv) % modulus)
        data[q] = _CRTData(q, p_list, modulus, bases)
    return data


def _subset_sums_mod(terms: List[int], mod: int) -> List[int]:
    sums = [0]
    for t in terms:
        sums += [(x + t) % mod for x in sums]
    return sums


def _q_for_p(p: int, prime_list: List[int]) -> int:
    for q in prime_list:
        if q * q > p:
            return q
    raise ValueError("q not found")


def _min_b_difference(p: int, crt: _CRTData) -> int:
    p_list = crt.primes_lt_q
    modulus = crt.modulus
    if not p_list:
        return 1

    terms = [(((-p) % r) * base) % modulus for r, base in zip(p_list, crt.bases)]
    k = len(terms)
    mid = k // 2

    left = _subset_sums_mod(terms[:mid], modulus)
    right = _subset_sums_mod(terms[mid:], modulus)
    right.sort()

    best: Optional[int] = None

    for arr in (left, right):
        for x in arr:
            if x != 0 and (x % p) != 0:
                if best is None or x < best:
                    best = x

    if best is None:
        best = modulus

    for l_val in left:
        target = modulus - l_val
        idx = bisect.bisect_left(right, target)
        j = idx
        while j < len(right):
            s = l_val + right[j]
            if s == modulus:
                j += 1
                continue
            if s < modulus:
                break
            res = s - modulus
            if res >= best:
                break
            if (res % p) != 0:
                best = res
                break
            j += 1

    return best


def _max_b_sum(p: int, crt: _CRTData) -> Optional[int]:
    p_list = crt.primes_lt_q
    modulus = crt.modulus
    limit = p // 2

    if not p_list:
        return limit

    amax = p - limit
    bmax = limit
    if modulus > amax * bmax:
        return None

    terms = [((p % r) * base) % modulus for r, base in zip(p_list, crt.bases)]
    residues = _subset_sums_mod(terms, modulus)

    best_b = 0
    for b0 in residues:
        if b0 == 0:
            if modulus <= limit:
                b_val = (limit // modulus) * modulus
                if b_val > best_b:
                    best_b = b_val
        else:
            if b0 <= limit:
                b_val = b0 + ((limit - b0) // modulus) * modulus
                if b_val > best_b:
                    best_b = b_val

    return None if best_b == 0 else best_b


def _v_of_prime(
    p: int, prime_qs: List[int], crt_by_q: Dict[int, _CRTData]
) -> int:
    q = _q_for_p(p, prime_qs)
    crt = crt_by_q[q]

    adiff = p + _min_b_difference(p, crt)
    bsum = _max_b_sum(p, crt)

    if bsum is None:
        return adiff
    asum = p - bsum
    return asum if asum < adiff else adiff


def solve(n: int = 3800) -> int:
    """Compute S(n) summing V(p) across all primes p < n using meet-in-the-middle CRT."""
    primes_all = _sieve(max(100, n + 10))
    primes_under_n = [p for p in primes_all if p < n]

    max_q_needed = 0
    for p in primes_under_n:
        q = _q_for_p(p, primes_all)
        if q > max_q_needed:
            max_q_needed = q
    prime_qs = [q for q in primes_all if q <= max_q_needed]

    crt_by_q = _build_crt_data(prime_qs)

    total = 0
    for p in primes_under_n:
        total += _v_of_prime(p, prime_qs, crt_by_q)

    return total


if __name__ == "__main__":
    print(solve())
