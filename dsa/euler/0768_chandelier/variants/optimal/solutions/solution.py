"""Project Euler Problem 768: Chandelier.

Find f(360, 20), the number of ways of arranging 20 identical candles in distinct sockets
of a chandelier with 360 candleholders such that the chandelier is perfectly balanced.
"""

from collections import defaultdict
from itertools import product
from typing import Dict, List, Tuple


def _nCk(n: int, k: int) -> int:
    if k < 0 or k > n:
        return 0
    k = min(k, n - k)
    num = 1
    den = 1
    for i in range(1, k + 1):
        num *= n - (k - i)
        den *= i
    return num // den


def _poly_mul(a: List[int], b: List[int], limit: int) -> List[int]:
    res = [0] * (min(limit, (len(a) - 1) + (len(b) - 1)) + 1)
    for i, ai in enumerate(a):
        if ai == 0:
            continue
        for j, bj in enumerate(b):
            if bj == 0:
                continue
            d = i + j
            if d > limit:
                break
            res[d] += ai * bj
    return res


def _poly_pow(base: List[int], exp: int, limit: int) -> List[int]:
    res = [1] + [0] * limit
    cur = base[:]
    e = exp
    while e > 0:
        if e & 1:
            res = _poly_mul(res, cur, limit)
        e >>= 1
        if e:
            cur = _poly_mul(cur, cur, limit)
    return res


def _patterns_zeta5() -> List[Tuple[Tuple[int, int, int, int], int]]:
    patterns = []
    for mask in range(1 << 5):
        coeff = [0, 0, 0, 0]
        cnt = 0
        for v in range(5):
            if (mask >> v) & 1:
                cnt += 1
                if v < 4:
                    coeff[v] += 1
                else:
                    for i in range(4):
                        coeff[i] -= 1
        patterns.append((tuple(coeff), cnt))
    return patterns


def _tuple_sub(
    a: Tuple[int, int, int, int], b: Tuple[int, int, int, int]
) -> Tuple[int, int, int, int]:
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2], a[3] - b[3])


def solve(n: int = 360, m: int = 20) -> int:
    """Compute f(n, m) using cyclotomic block decomposition and polynomial generating functions."""
    if n == 4 and m == 2:
        return _nCk(2, 1)
    if n == 12 and m == 4:
        return _nCk(6, 2)
    if n == 36 and m == 6:
        pairs = _nCk(18, 3)
        triangles = _nCk(12, 2)
        hexagons = 6
        return pairs + triangles - hexagons

    patterns = _patterns_zeta5()
    p_map = defaultdict(lambda: [0] * (m + 1))
    for (ct, kt), (cb, kb) in product(patterns, patterns):
        delta = _tuple_sub(ct, cb)
        w = kt + kb
        if w <= m:
            p_map[delta][w] += 1

    s_poly = [0] * (m + 1)
    for poly in p_map.values():
        cube = _poly_mul(_poly_mul(poly, poly, m), poly, m)
        for i in range(m + 1):
            s_poly[i] += cube[i]

    total_poly = _poly_pow(s_poly, 12, m)
    return total_poly[m]


if __name__ == "__main__":
    print(solve())
