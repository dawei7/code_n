"""Project Euler Problem 463: A Weird Recurrence Relation.

Find S(3^37) mod 10^9, where S(n) = sum_{i=1..n} f(i) and f(n) satisfies:
f(1) = 1, f(3) = 3, f(2n) = f(n), f(4n+1) = 2f(2n+1) - f(n), f(4n+3) = 3f(2n+1) - 2f(n).
"""

from typing import Tuple

MOD = 1_000_000_000


def _mat_mul_2x2(
    x_mat: Tuple[Tuple[int, int], Tuple[int, int]],
    y_mat: Tuple[Tuple[int, int], Tuple[int, int]],
    mod: int = MOD,
) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    return (
        (
            (x_mat[0][0] * y_mat[0][0] + x_mat[0][1] * y_mat[1][0]) % mod,
            (x_mat[0][0] * y_mat[0][1] + x_mat[0][1] * y_mat[1][1]) % mod,
        ),
        (
            (x_mat[1][0] * y_mat[0][0] + x_mat[1][1] * y_mat[1][0]) % mod,
            (x_mat[1][0] * y_mat[0][1] + x_mat[1][1] * y_mat[1][1]) % mod,
        ),
    )


def _mat_pow_2x2(
    m_mat: Tuple[Tuple[int, int], Tuple[int, int]],
    exp: int,
    mod: int = MOD,
) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    res = ((1, 0), (0, 1))
    base = (
        (m_mat[0][0] % mod, m_mat[0][1] % mod),
        (m_mat[1][0] % mod, m_mat[1][1] % mod),
    )
    while exp > 0:
        if exp & 1:
            res = _mat_mul_2x2(res, base, mod)
        base = _mat_mul_2x2(base, base, mod)
        exp >>= 1
    return res


M0 = ((1, 0), (-1, 2))
M1 = ((0, 1), (-2, 3))
A_MAT = (
    (M0[0][0] + M1[0][0], M0[0][1] + M1[0][1]),
    (M0[1][0] + M1[1][0], M0[1][1] + M1[1][1]),
)


def _vk(k: int, mod: int = MOD) -> Tuple[int, int]:
    if k == 1:
        return 1, 3
    a, b = 1, 3
    for ch in bin(k)[3:]:
        if ch == "0":
            a, b = a, (-a + 2 * b) % mod
        else:
            a, b = b, (-2 * a + 3 * b) % mod
    return a % mod, b % mod


def _sum_interval(k: int, d: int, mod: int = MOD) -> int:
    a, b = _vk(k, mod)
    p_mat = _mat_pow_2x2(A_MAT, d, mod)
    r0, r1 = p_mat[0]
    return (r0 * a + r1 * b) % mod


def solve(n: int = 3**37, mod: int = MOD) -> int:
    """Compute S(n) mod mod using dyadic interval decomposition and binary matrix transitions."""
    res = 0
    pos = 1
    while pos <= n:
        remaining = n - pos + 1
        tz = (pos & -pos).bit_length() - 1
        d = min(tz, remaining.bit_length() - 1)
        size = 1 << d
        k = pos >> d
        res = (res + _sum_interval(k, d, mod)) % mod
        pos += size
    return res


if __name__ == "__main__":
    print(solve())
