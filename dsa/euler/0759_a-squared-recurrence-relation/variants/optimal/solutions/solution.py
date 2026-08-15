"""Project Euler Problem 759: A Squared Recurrence Relation.

Find S(10^16) modulo 1000000007, where S(n) = sum_{i=1}^n f(i)^2 and f(n) = n * popcount(n).
"""

from typing import List

_MOD = 1_000_000_007

Matrix3x3 = List[List[int]]


def _zero_mat() -> Matrix3x3:
    return [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def _add_mat(a: Matrix3x3, b: Matrix3x3) -> Matrix3x3:
    return [
        [
            (a[0][0] + b[0][0]) % _MOD,
            (a[0][1] + b[0][1]) % _MOD,
            (a[0][2] + b[0][2]) % _MOD,
        ],
        [
            (a[1][0] + b[1][0]) % _MOD,
            (a[1][1] + b[1][1]) % _MOD,
            (a[1][2] + b[1][2]) % _MOD,
        ],
        [
            (a[2][0] + b[2][0]) % _MOD,
            (a[2][1] + b[2][1]) % _MOD,
            (a[2][2] + b[2][2]) % _MOD,
        ],
    ]


def _shift_range(mat: Matrix3x3, p: int) -> Matrix3x3:
    p_mod = p % _MOD
    p2 = (p_mod * p_mod) % _MOD
    two_p = (2 * p_mod) % _MOD

    mats = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for t in (0, 1, 2):
        s0 = mat[t][0] % _MOD
        s1 = mat[t][1] % _MOD
        s2 = mat[t][2] % _MOD
        mats[t][0] = s0
        mats[t][1] = (p_mod * s0 + s1) % _MOD
        mats[t][2] = (p2 * s0 + two_p * s1 + s2) % _MOD

    coeffs = (
        (1, 0, 0),
        (1, 1, 0),
        (1, 2, 1),
    )

    out = _zero_mat()
    for j in (0, 1, 2):
        c0, c1, c2 = coeffs[j]
        for d in (0, 1, 2):
            out[j][d] = (c0 * mats[0][d] + c1 * mats[1][d] + c2 * mats[2][d]) % _MOD
    return out


def _calc_upto(n: int, full: List[Matrix3x3]) -> Matrix3x3:
    if n < 0:
        return _zero_mat()
    if n == 0:
        return full[0]

    k = n.bit_length() - 1
    p = 1 << k
    if n == p - 1:
        return full[k]

    r = n - p
    return _add_mat(full[k], _shift_range(_calc_upto(r, full), p))


def solve(n: int = 10_000_000_000_000_000) -> int:
    """Compute S(n) modulo 1000000007 using binary digit moment divide-and-conquer DP."""
    max_bits = max(60, n.bit_length())
    full = [_zero_mat() for _ in range(max_bits + 1)]
    full[0][0][0] = 1

    for m in range(1, max_bits + 1):
        p = 1 << (m - 1)
        full[m] = _add_mat(full[m - 1], _shift_range(full[m - 1], p))

    res_mat = _calc_upto(n, full)
    return res_mat[2][2] % _MOD


if __name__ == "__main__":
    print(solve())
