"""Project Euler Problem 758: Buckets of Water.

Find the sum of P(2^{p^5}-1, 2^{q^5}-1) modulo 1000000007 for all pairs of prime
numbers p < q < 1000, where P(a, b) is the minimal number of pourings to get 1 litre.
"""

from typing import Dict, List, Tuple

_MOD = 1_000_000_007


def _primes_below(n: int) -> List[int]:
    if n <= 2:
        return []
    sieve = bytearray(b"\x01") * n
    sieve[0:2] = b"\x00\x00"
    p = 2
    while p * p < n:
        if sieve[p]:
            step = p
            start = p * p
            sieve[start:n:step] = b"\x00" * (((n - 1 - start) // step) + 1)
        p += 1
    return [i for i in range(2, n) if sieve[i]]


def _penultimate_convergent_mod(
    cf_terms_mod: List[int], mod: int = _MOD
) -> Tuple[int, int]:
    p_m2, p_m1 = 0, 1
    q_m2, q_m1 = 1, 0
    convs: List[Tuple[int, int]] = []
    for a in cf_terms_mod:
        p = (a * p_m1 + p_m2) % mod
        q = (a * q_m1 + q_m2) % mod
        convs.append((p, q))
        p_m2, p_m1 = p_m1, p
        q_m2, q_m1 = q_m1, q

    return convs[0] if len(convs) == 1 else convs[-2]


def _geom_sum_ratio(ratio: int, m: int, inv_cache: Dict[int, int]) -> int:
    if m <= 0:
        return 0
    ratio %= _MOD
    if ratio == 1:
        return m % _MOD
    inv = inv_cache.get(ratio)
    if inv is None:
        inv = pow((ratio - 1) % _MOD, _MOD - 2, _MOD)
        inv_cache[ratio] = inv
    return ((pow(ratio, m, _MOD) - 1) % _MOD) * inv % _MOD


def _cf_terms_mersenne_exponents(
    e_small: int, e_large: int, inv_cache: Dict[int, int]
) -> List[int]:
    terms: List[int] = []
    hi, lo = e_large, e_small
    while True:
        m, r = divmod(hi, lo)
        ratio = pow(2, lo, _MOD)
        shift = pow(2, r, _MOD)
        series = _geom_sum_ratio(ratio, m, inv_cache)
        q_mod = (shift * series) % _MOD
        terms.append(q_mod)
        if r == 0:
            break
        hi, lo = lo, r
    return terms


def _p_mersenne_exponents_mod(
    ea: int, eb: int, inv_cache: Dict[int, int]
) -> int:
    terms_mod = _cf_terms_mersenne_exponents(ea, eb, inv_cache)
    pen_p, pen_q = _penultimate_convergent_mod(terms_mod, _MOD)
    return (2 * ((pen_p + pen_q) % _MOD) - 2) % _MOD


def solve(limit: int = 1000) -> int:
    """Compute sum P(2^{p^5}-1, 2^{q^5}-1) mod 1000000007 using Mersenne exponent continued fraction reduction."""
    primes = _primes_below(limit)
    exps = [p**5 for p in primes]
    inv_cache: Dict[int, int] = {}

    total = 0
    for i in range(len(primes)):
        ea = exps[i]
        for j in range(i + 1, len(primes)):
            eb = exps[j]
            total = (total + _p_mersenne_exponents_mod(ea, eb, inv_cache)) % _MOD

    return total


if __name__ == "__main__":
    print(solve())
