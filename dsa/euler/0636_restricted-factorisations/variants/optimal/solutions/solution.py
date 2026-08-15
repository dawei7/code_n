"""Project Euler Problem 636: Restricted Factorisations.

Find F(1000000!) mod 1000000007, where F(n) is the number of ways to write n
as a product of one 1st power, two squares, three cubes, and four 4th powers with distinct bases.
"""

from collections import Counter, defaultdict
import math
from typing import Dict, Generator, List, Tuple

_MOD = 1_000_000_007
_SLOT_WEIGHTS = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
_TOTAL_WEIGHT = sum(_SLOT_WEIGHTS)
_D = 30


def _primes_upto(n: int) -> List[int]:
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[:2] = b"\x00\x00"
    r = int(math.isqrt(n))
    for i in range(2, r + 1):
        if sieve[i]:
            step = i
            start = i * i
            sieve[start : n + 1 : step] = b"\x00" * (((n - start) // step) + 1)
    return [i for i in range(n + 1) if sieve[i]]


def _factorial_prime_exp(n: int, p: int) -> int:
    e = 0
    while n:
        n //= p
        e += n
    return e


def _gen_partitions(n: int) -> Generator[List[List[int]], None, None]:
    def helper(
        i: int, blocks: List[List[int]]
    ) -> Generator[List[List[int]], None, None]:
        if i == n:
            yield [b[:] for b in blocks]
            return
        for b in blocks:
            b.append(i)
            yield from helper(i + 1, blocks)
            b.pop()
        blocks.append([i])
        yield from helper(i + 1, blocks)
        blocks.pop()

    yield from helper(0, [])


def _build_partition_coefficients() -> Dict[Tuple[int, ...], int]:
    coeff: Dict[Tuple[int, ...], int] = defaultdict(int)
    for blocks in _gen_partitions(10):
        mu = 1
        sums = []
        for b in blocks:
            s = len(b)
            mu *= ((-1) ** (s - 1)) * math.factorial(s - 1)
            wsum = sum(_SLOT_WEIGHTS[idx] for idx in b)
            sums.append(wsum)
        key = tuple(sorted(sums))
        coeff[key] += mu
    return coeff


def _coeffs_up_to(key: Tuple[int, ...], limit: int) -> List[int]:
    dp = [0] * (limit + 1)
    dp[0] = 1
    for w in key:
        for i in range(w, limit + 1):
            v = dp[i] + dp[i - w]
            if v >= _MOD:
                v -= _MOD
            dp[i] = v
    return dp


def _poly_q_from_key(key: Tuple[int, ...]) -> List[int]:
    q = [0] * (_TOTAL_WEIGHT + 1)
    q[0] = 1
    for w in key:
        for i in range(_TOTAL_WEIGHT - w, -1, -1):
            q[i + w] -= q[i]
    return q


def _mul_mod_poly(a: List[int], b: List[int], r: List[int]) -> List[int]:
    tmp = [0] * (2 * _D - 1)
    for i in range(_D):
        ai = a[i]
        if ai:
            for j in range(_D):
                tmp[i + j] = (tmp[i + j] + ai * b[j]) % _MOD
    for k in range(2 * _D - 2, _D - 1, -1):
        coef = tmp[k]
        if coef:
            for i in range(1, _D + 1):
                tmp[k - i] = (tmp[k - i] + coef * r[i - 1]) % _MOD
    return tmp[:_D]


def _precompute_powers_of_x(r: List[int], maxbit: int = 20) -> List[List[int]]:
    pow_polys = [[0] * _D for _ in range(maxbit)]
    pow_polys[0][1] = 1
    for b in range(1, maxbit):
        pow_polys[b] = _mul_mod_poly(pow_polys[b - 1], pow_polys[b - 1], r)
    return pow_polys


def _poly_x_n(
    pow_polys: List[List[int]], n: int, r: List[int]
) -> List[int]:
    res = [0] * _D
    res[0] = 1
    bit = 0
    p = n
    while p:
        if p & 1:
            res = _mul_mod_poly(res, pow_polys[bit], r)
        p >>= 1
        bit += 1
    return res


def _term_from_poly(init: List[int], poly: List[int]) -> int:
    s = 0
    for ci, ai in zip(poly, init):
        s = (s + ci * ai) % _MOD
    return s


def solve(n: int = 1_000_000) -> int:
    """Compute F(n!) modulo 1000000007 using set-partition inclusion-exclusion and Fiduccia's linear recurrence."""
    primes = _primes_upto(n)
    coeff_dict = _build_partition_coefficients()

    freq = Counter()
    for p in primes:
        if p > n:
            break
        e = _factorial_prime_exp(n, p)
        freq[e] += 1

    inv288 = pow(288, _MOD - 2, _MOD)
    exps_sorted = sorted(freq)
    max_exp = exps_sorted[-1]
    use_cutoff = min(13000, max_exp)
    large_exps = [e for e in exps_sorted if e > use_cutoff]

    if freq.get(1, 0):
        keys = [k for k in coeff_dict if 1 in k]
    else:
        keys = list(coeff_dict.keys())

    items = list(freq.items())
    total = 0
    maxbit = 20

    for key in keys:
        dp = _coeffs_up_to(key, use_cutoff)
        large_vals: Dict[int, int] = {}
        if large_exps:
            q = _poly_q_from_key(key)
            r = [(-q[i]) % _MOD for i in range(1, _TOTAL_WEIGHT + 1)]
            pow_polys = _precompute_powers_of_x(r, maxbit=maxbit)
            init = dp[:_D] + [0] * max(0, _D - len(dp))
            for e in large_exps:
                poly = _poly_x_n(pow_polys, e, r)
                large_vals[e] = _term_from_poly(init, poly)

        prod = 1
        for e, cnt in items:
            val = dp[e] if e <= use_cutoff else large_vals[e]
            if val == 0:
                prod = 0
                break
            prod = (prod * pow(val, cnt, _MOD)) % _MOD

        if prod:
            total = (total + (coeff_dict[key] % _MOD) * prod) % _MOD

    return (total * inv288) % _MOD


if __name__ == "__main__":
    print(solve())
