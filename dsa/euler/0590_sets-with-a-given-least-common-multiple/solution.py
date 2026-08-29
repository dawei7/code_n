"""Project Euler Problem 590: Sets with a Given Least Common Multiple.

Find HL(50000) modulo 10^9, where HL(n) = H(L(n)) is the number of sets of positive
integers whose least common multiple equals L(n) = lcm(1, ..., n).
"""

from collections import defaultdict
from math import gcd
from typing import Dict, List, Tuple

_MOD = 10**9
_MOD2 = 2**9
_MOD5 = 5**9
_PHI5 = 4 * 5**8


def _lcm(a: int, b: int) -> int:
    return a // gcd(a, b) * b


def _sieve(limit: int) -> List[int]:
    if limit < 2:
        return []
    is_prime = bytearray(b"\x01") * (limit + 1)
    is_prime[0:2] = b"\x00\x00"
    p = 2
    while p * p <= limit:
        if is_prime[p]:
            step = p
            start = p * p
            is_prime[start : limit + 1 : step] = b"\x00" * (
                ((limit - start) // step) + 1
            )
        p += 1
    return [i for i in range(limit + 1) if is_prime[i]]


def _max_power_exponent(p: int, n: int) -> int:
    e = 1
    pp = p
    while pp * p <= n:
        pp *= p
        e += 1
    return e


def _factorize(n: int) -> List[Tuple[int, int]]:
    res: List[Tuple[int, int]] = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            e = 0
            while n % d == 0:
                n //= d
                e += 1
            res.append((d, e))
        d += 1 if d == 2 else 2
    if n > 1:
        res.append((n, 1))
    return res


def _h_small(n: int) -> int:
    if n == 1:
        return 1
    factors = _factorize(n)
    primes = [p for p, _ in factors]
    exps = [e for _, e in factors]
    k = len(primes)

    total = 0
    for mask in range(1 << k):
        bits = 0
        divcount = 1
        for i in range(k):
            if (mask >> i) & 1:
                bits += 1
                divcount *= exps[i]
            else:
                divcount *= exps[i] + 1
        term = 1 << divcount
        if bits & 1:
            total -= term
        else:
            total += term
    return total


def _hl_small(n: int) -> int:
    l_val = 1
    for i in range(1, n + 1):
        l_val = _lcm(l_val, i)
    return _h_small(l_val)


def _binom_coeffs_signed_mod(n: int, mod: int) -> List[int]:
    coeffs = [0] * (n + 1)
    c = 1
    for k in range(n + 1):
        if ((n - k) & 1) == 0:
            coeffs[k] = c % mod
        else:
            coeffs[k] = (-c) % mod
        if k != n:
            c = c * (n - k) // (k + 1)
    return coeffs


def _group_terms(
    exponent: int, count: int, mod_phi: int, mod_w: int
) -> List[Tuple[int, int]]:
    out: List[Tuple[int, int]] = []
    c = 1
    for t in range(count + 1):
        mul = (
            pow(exponent, t, mod_phi) * pow(exponent + 1, count - t, mod_phi)
        ) % mod_phi
        w = c
        if t & 1:
            w = -w
        out.append((mul, w % mod_w))
        if t != count:
            c = c * (count - t) // (t + 1)
    return out


def _eval_f_r(x_mod_phi: int, coeffs: List[int]) -> int:
    mod = _MOD5
    p = pow(2, x_mod_phi, mod)
    acc = 0
    for i, ck in enumerate(coeffs):
        acc += ck * p
        if (i & 63) == 63:
            acc %= mod
        p = (p * p) % mod
    return acc % mod


def solve(n: int = 50000) -> int:
    """Compute HL(n) modulo 10^9 using prime power group DP, repeated squaring, and CRT."""
    if n <= 10:
        return _hl_small(n) % _MOD

    primes = _sieve(n)
    r = 0
    counts: Dict[int, int] = defaultdict(int)
    for p in primes:
        a = _max_power_exponent(p, n)
        if a == 1:
            r += 1
        else:
            counts[a] += 1

    dist: Dict[int, int] = {1: 1}
    for a in sorted(counts):
        c = counts[a]
        terms = _group_terms(a, c, _PHI5, _MOD5)
        new_dist: Dict[int, int] = defaultdict(int)
        for x_prev, w_prev in dist.items():
            for mul, w in terms:
                new_x = (x_prev * mul) % _PHI5
                new_dist[new_x] = (new_dist[new_x] + w_prev * w) % _MOD5
        dist = new_dist

    coeffs = _binom_coeffs_signed_mod(r, _MOD5)

    total_mod5 = 0
    for x_mod, w in dist.items():
        if w:
            total_mod5 = (total_mod5 + w * _eval_f_r(x_mod, coeffs)) % _MOD5

    inv_512 = pow(_MOD2, -1, _MOD5)
    t = (total_mod5 * inv_512) % _MOD5
    return (_MOD2 * t) % _MOD


if __name__ == "__main__":
    print(solve())
