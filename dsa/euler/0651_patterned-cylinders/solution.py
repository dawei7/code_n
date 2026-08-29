"""Project Euler Problem 651: Patterned Cylinders.

Find sum_{i=4}^40 f(i, F_{i-1}, F_i) mod 1000000007, where f(m, a, b) is the number of distinct
periodic patterns on an a x b cylinder using exactly m colours under cylinder symmetries.
"""

from collections import defaultdict
import math
from typing import Dict, List, Tuple

_MOD = 1_000_000_007


def _sieve(limit: int) -> List[int]:
    if limit < 2:
        return []
    bs = bytearray(b"\x01") * (limit + 1)
    bs[0:2] = b"\x00\x00"
    r = int(limit**0.5)
    for i in range(2, r + 1):
        if bs[i]:
            step = i
            start = i * i
            bs[start : limit + 1 : step] = b"\x00" * (
                ((limit - start) // step) + 1
            )
    return [i for i in range(limit + 1) if bs[i]]


_PRIMES = _sieve(20_000)


def _factorize(n: int) -> Dict[int, int]:
    f: Dict[int, int] = {}
    x = n
    for p in _PRIMES:
        if p * p > x:
            break
        if x % p == 0:
            e = 0
            while x % p == 0:
                x //= p
                e += 1
            f[p] = e
    if x > 1:
        f[x] = f.get(x, 0) + 1
    return f


def _divisors_and_phi(factors: Dict[int, int]) -> List[Tuple[int, int]]:
    res = [(1, 1)]
    for p, e in factors.items():
        new: List[Tuple[int, int]] = []
        pk = 1
        for k in range(e + 1):
            phi_pk = 1 if k == 0 else (pk // p) * (p - 1)
            for d, ph in res:
                new.append((d * pk, ph * phi_pk))
            pk *= p
        res = new
    return res


def _dihedral_types(n: int) -> List[Tuple[Dict[int, int], int]]:
    fac = _factorize(n)
    div_phi = _divisors_and_phi(fac)
    types: List[Tuple[Dict[int, int], int]] = []

    for length, phi_len in div_phi:
        types.append(({length: n // length}, phi_len))

    if n % 2 == 1:
        types.append(({1: 1, 2: (n - 1) // 2}, n))
    else:
        types.append(({1: 2, 2: (n - 2) // 2}, n // 2))
        types.append(({2: n // 2}, n // 2))

    return types


def _cycles_on_grid(dist_a: Dict[int, int], dist_b: Dict[int, int]) -> int:
    total = 0
    for la, ca in dist_a.items():
        for lb, cb in dist_b.items():
            total += ca * cb * math.gcd(la, lb)
    return total


def _f_exact(m: int, a: int, b: int) -> int:
    comb = [math.comb(m, k) for k in range(m + 1)]
    types_a = _dihedral_types(a)
    types_b = _dihedral_types(b)

    cycle_mult: Dict[int, int] = defaultdict(int)
    for da, ma in types_a:
        for db, mb in types_b:
            c = _cycles_on_grid(da, db)
            cycle_mult[c] = (cycle_mult[c] + (ma * mb) % _MOD) % _MOD

    fixed_sum = 0
    cache: Dict[int, int] = {}
    for c, mult in cycle_mult.items():
        val = cache.get(c)
        if val is None:
            surj = 0
            for k in range(m + 1):
                term = (comb[k] * pow(m - k, c, _MOD)) % _MOD
                if k % 2 == 1:
                    surj = (surj - term + _MOD) % _MOD
                else:
                    surj = (surj + term) % _MOD
            val = surj
            cache[c] = val
        fixed_sum = (fixed_sum + mult * val) % _MOD

    group_size = (4 * (a % _MOD) * (b % _MOD)) % _MOD
    inv_group = pow(group_size, _MOD - 2, _MOD)
    return (fixed_sum * inv_group) % _MOD


def solve(max_i: int = 40) -> int:
    """Compute sum_{i=4}^max_i f(i, F_{i-1}, F_i) mod 1000000007 using Pólya enumeration on D_a x D_b."""
    fib = [0, 1]
    for _ in range(2, max_i + 2):
        fib.append(fib[-1] + fib[-2])

    total = 0
    for i in range(4, max_i + 1):
        val = _f_exact(i, fib[i - 1], fib[i])
        total = (total + val) % _MOD

    return total


if __name__ == "__main__":
    print(solve())
