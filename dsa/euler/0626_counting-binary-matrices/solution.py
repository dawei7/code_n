"""Project Euler Problem 626: Counting Binary Matrices.

Find c(20) mod 1001001011, where c(n) is the number of non-equivalent n x n binary matrices
under row/column permutations and row/column bit flips.
"""

from math import gcd
from typing import Dict, Generator, List, Tuple

_MOD = 1_001_001_011


def _v2(x: int) -> int:
    c = 0
    while x % 2 == 0:
        x //= 2
        c += 1
    return c


def _max_v2_upto(n: int) -> int:
    t = 0
    p = 1
    while p * 2 <= n:
        p *= 2
        t += 1
    return t


def _partitions(
    n: int, max_part: int | None = None
) -> Generator[List[int], None, None]:
    if max_part is None or max_part > n:
        max_part = n
    if n == 0:
        yield []
        return
    for first in range(min(max_part, n), 0, -1):
        for rest in _partitions(n - first, first):
            yield [first] + rest


class _PartInfo:
    __slots__ = ("lens_mults", "k_cycles", "tmin", "prefix_lt", "count_mod")

    def __init__(
        self,
        lens_mults: List[Tuple[int, int]],
        k_cycles: int,
        tmin: int,
        prefix_lt: List[int],
        count_mod: int,
    ):
        self.lens_mults = lens_mults
        self.k_cycles = k_cycles
        self.tmin = tmin
        self.prefix_lt = prefix_lt
        self.count_mod = count_mod


def _build_part_infos(
    n: int, mod: int
) -> Tuple[List[_PartInfo], List[int]]:
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = (fact[i - 1] * i) % mod

    invfact = [1] * (n + 1)
    invfact[n] = pow(fact[n], mod - 2, mod)
    for i in range(n, 0, -1):
        invfact[i - 1] = (invfact[i] * i) % mod

    inv_int = [0] * (n + 1)
    for i in range(1, n + 1):
        inv_int[i] = pow(i, mod - 2, mod)

    tmax = _max_v2_upto(n)
    infos: List[_PartInfo] = []

    for p in _partitions(n):
        counts: Dict[int, int] = {}
        for x in p:
            counts[x] = counts.get(x, 0) + 1

        lens_mults = sorted(counts.items())
        k_cycles = len(p)
        tmin = min(_v2(length) for length in counts)

        count_v2 = [0] * (tmax + 1)
        for length, mult in counts.items():
            count_v2[_v2(length)] += mult

        prefix_lt = [0] * (tmax + 2)
        s = 0
        for t in range(tmax + 1):
            s += count_v2[t]
            prefix_lt[t + 1] = s

        count_mod = fact[n]
        for length, mult in counts.items():
            count_mod = (count_mod * pow(inv_int[length], mult, mod)) % mod
            count_mod = (count_mod * invfact[mult]) % mod

        infos.append(_PartInfo(lens_mults, k_cycles, tmin, prefix_lt, count_mod))

    return infos, fact


def solve(n: int = 20) -> int:
    """Compute c(n) mod 1001001011 using Burnside's Lemma over row/col signed cycle types."""
    infos, fact = _build_part_infos(n, _MOD)

    gcd_tab = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            gcd_tab[i][j] = gcd(i, j)

    pow2 = [1] * (n * n + 1)
    for i in range(1, n * n + 1):
        pow2[i] = (pow2[i - 1] * 2) % _MOD

    total = 0
    for pr in infos:
        for pc in infos:
            cycles = 0
            for lr, mr in pr.lens_mults:
                for lc, mc in pc.lens_mults:
                    cycles += mr * mc * gcd_tab[lr][lc]

            tr, tc = pr.tmin, pc.tmin
            if tr < tc:
                d = pr.prefix_lt[tc]
            elif tc < tr:
                d = pc.prefix_lt[tr]
            else:
                d = 1

            e = cycles - pr.k_cycles - pc.k_cycles + d
            term = (pr.count_mod * pc.count_mod) % _MOD
            term = (term * pow2[e]) % _MOD
            total = (total + term) % _MOD

    inv_fact_n = pow(fact[n], _MOD - 2, _MOD)
    inv_den = (inv_fact_n * inv_fact_n) % _MOD
    return (total * inv_den) % _MOD


if __name__ == "__main__":
    print(solve())
