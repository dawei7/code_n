"""Project Euler Problem 682: 5-Smooth Pairs.

Find f(10^7) mod 1000000007, where f(n) is the number of pairs (p, q) of 5-smooth (Hamming) numbers
such that Omega(p) = Omega(q) and s(p) + s(q) = n.
"""

from typing import List, Tuple

_MOD = 1_000_000_007


def _poly_trim(p: List[int]) -> List[int]:
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def _poly_mul(a: List[int], b: List[int]) -> List[int]:
    if a == [0] or b == [0]:
        return [0]
    res = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                if bj:
                    res[i + j] = (res[i + j] + ai * bj) % _MOD
    return res


def _poly_from_1_minus_xk(k: int) -> List[int]:
    p = [0] * (k + 1)
    p[0] = 1
    p[k] = _MOD - 1
    return p


def _negate_odd_coeffs(p: List[int]) -> List[int]:
    q = p[:]
    for i in range(1, len(q), 2):
        q[i] = (-q[i]) % _MOD
    return q


def _even_part(p: List[int]) -> List[int]:
    return p[::2] if len(p) > 1 else p[:]


def _odd_part(p: List[int]) -> List[int]:
    out = p[1::2]
    return out if out else [0]


def _build_generating_function_pq() -> Tuple[List[int], List[int]]:
    def mul_factors(factors: List[List[int]]) -> List[int]:
        out = [1]
        for f in factors:
            out = _poly_mul(out, f)
        return out

    d1 = mul_factors([_poly_from_1_minus_xk(k) for k in (1, 3, 4, 5, 7)])
    d2 = mul_factors(
        [[1, _MOD - 1], [1, _MOD - 1], [1, 1]]
        + [_poly_from_1_minus_xk(k) for k in (5, 6, 8)]
    )
    d3 = mul_factors(
        [[1, _MOD - 1], [1, _MOD - 1], [1, 1], [1, 1, 1]]
        + [_poly_from_1_minus_xk(k) for k in (7, 8, 10)]
    )

    q = _poly_mul(_poly_mul(d1, d2), d3)

    q_over_d1 = _poly_mul(d2, d3)
    q_over_d2 = _poly_mul(d1, d3)
    q_over_d3 = _poly_mul(d1, d2)

    p1 = q_over_d1
    p2 = [0] + q_over_d2
    p2 = [(-c) % _MOD for c in p2]
    p3 = [0] * 5 + q_over_d3

    n_deg = max(len(p1), len(p2), len(p3))
    p = [0] * n_deg
    for i in range(n_deg):
        c1 = p1[i] if i < len(p1) else 0
        c2 = p2[i] if i < len(p2) else 0
        c3 = p3[i] if i < len(p3) else 0
        p[i] = (c1 + c2 + c3) % _MOD

    return p, q


def solve(n: int = 10_000_000) -> int:
    """Compute f(n) modulo 1000000007 using the rational generating function and Bostan-Mori algorithm."""
    p_cur, q_cur = _build_generating_function_pq()
    power = n
    while power > 0:
        q_neg = _negate_odd_coeffs(q_cur)
        p_cur = _poly_mul(p_cur, q_neg)
        q_cur = _poly_mul(q_cur, q_neg)

        if power & 1:
            p_cur = _odd_part(p_cur)
        else:
            p_cur = _even_part(p_cur)
        q_cur = _even_part(q_cur)

        _poly_trim(p_cur)
        _poly_trim(q_cur)
        power >>= 1

    ans = p_cur[0] * pow(q_cur[0], _MOD - 2, _MOD) % _MOD
    return ans


if __name__ == "__main__":
    print(solve())
