"""Project Euler Problem 520: Simbers.

Find sum_{u=1..39} Q(2^u) mod 1_000_000_123, where Q(n) is the count of simbers
with at most n digits (odd digits appear odd times, even digits appear even times).
"""

from typing import Dict

MOD = 1_000_000_123
INV2 = pow(2, MOD - 2, MOD)


def _poly_mul(p: Dict[int, int], q: Dict[int, int]) -> Dict[int, int]:
    r: Dict[int, int] = {}
    for e1, c1 in p.items():
        for e2, c2 in q.items():
            e = e1 + e2
            r[e] = (r.get(e, 0) + c1 * c2) % MOD
    return r


def _poly_pow(p: Dict[int, int], n: int) -> Dict[int, int]:
    r: Dict[int, int] = {0: 1}
    base = p
    exp = n
    while exp > 0:
        if exp & 1:
            r = _poly_mul(r, base)
        base = _poly_mul(base, base)
        exp >>= 1
    return r


COSH = {1: INV2, -1: INV2}
SINH = {1: INV2, -1: (-INV2) % MOD}
ONE_PLUS_SINH = {0: 1, 1: INV2, -1: (-INV2) % MOD}

F_EGF = _poly_mul(_poly_pow(COSH, 5), _poly_pow(ONE_PLUS_SINH, 5))
G_EGF = _poly_mul(
    _poly_mul(SINH, _poly_pow(COSH, 4)), _poly_pow(ONE_PLUS_SINH, 5)
)

INV_T_MINUS_1: Dict[int, int] = {}
for t_val in range(-10, 11):
    tm = t_val % MOD
    if tm != 1:
        INV_T_MINUS_1[tm] = pow((tm - 1) % MOD, MOD - 2, MOD)


def _geom_sum_start1(t: int, n: int) -> int:
    if n <= 0:
        return 0
    tm = t % MOD
    if tm == 1:
        return n % MOD
    if tm == 0:
        return 0
    num = (pow(tm, n + 1, MOD) - tm) % MOD
    return num * INV_T_MINUS_1[tm] % MOD


def _geom_sum_start0(t: int, n: int) -> int:
    if n <= 0:
        return 0
    tm = t % MOD
    if tm == 1:
        return n % MOD
    num = (pow(tm, n, MOD) - 1) % MOD
    return num * INV_T_MINUS_1[tm] % MOD


def q_simbers(n: int) -> int:
    """Count simbers with at most n digits using Exponential Generating Functions."""
    sum_a = 0
    sum_c = 0

    for t, coef in F_EGF.items():
        sum_a = (sum_a + coef * _geom_sum_start1(t, n)) % MOD

    for t, coef in G_EGF.items():
        sum_c = (sum_c + coef * _geom_sum_start0(t, n)) % MOD

    return (sum_a - sum_c) % MOD


def solve(max_u: int = 39, mod: int = MOD) -> int:
    """Compute sum_{u=1..max_u} Q(2^u) mod mod using EGF geometric progressions."""
    total = 0
    for u in range(1, max_u + 1):
        total = (total + q_simbers(1 << u)) % mod
    return total


if __name__ == "__main__":
    print(solve())
