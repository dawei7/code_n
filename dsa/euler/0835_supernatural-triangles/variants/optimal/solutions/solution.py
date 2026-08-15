"""Project Euler Problem 835: Supernatural Triangles.

Mathematical reduction:
A Pythagorean triangle with sides a <= b < c is supernatural if two sides are consecutive.
There are two disjoint families (except for the single overlap (3, 4, 5)):

Family 1: Consecutive legs (b = a + 1)
  a^2 + (a+1)^2 = c^2  <=>  (2a+1)^2 - 2c^2 = -1
  Solutions (X_n, Y_n) with X_n = 2a+1, Y_n = c are given by (1 + sqrt(2))^{2n-1}.
  The perimeters P_n = X_n + Y_n satisfy the linear recurrence:
    P_1 = 2 (degenerate), P_2 = 12, P_{n+1} = 6 P_n - P_{n-1}
  The sum of perimeters up to n_max is:
    sum_{n=2}^{n_max} P_n = (P_{n_max+1} - P_{n_max} - 10) / 4
  For N = 10^{10^{10}}, n_max = floor( (10^{10} ln 10 + ln(2 sqrt(2))) / ln(3 + 2 sqrt(2)) ) = 13062480694.
  P_{n_max} and P_{n_max+1} are computed via 2x2 matrix exponentiation modulo 1234567891.

Family 2: Consecutive hypotenuse and leg (c = b + 1)
  a^2 + b^2 = (b+1)^2  <=>  b = (a^2 - 1) / 2
  Thus a = 2m + 1 >= 3 (odd integer), b = 2m(m+1), c = 2m(m+1) + 1.
  Perimeter P(m) = (2m+1)(2m+2) = 4m^2 + 6m + 2.
  Condition P(m) <= N with N = 10^{10^{10}} gives:
    a <= 10^{5 * 10^9} - 1 (odd)  =>  m_max = (10^{5 * 10^9} - 2) / 2
  By Fermat's Little Theorem:
    10^{5 * 10^9} mod M = 10^{(5 * 10^9) mod (M - 1)} mod M
  The polynomial sum sum_{m=1}^{m_max} (4m^2 + 6m + 2) is evaluated using Faulhaber formulas in O(1).

Overlap:
  The only triangle belonging to both families is (3, 4, 5) with perimeter 12.
  Total S(N) = (S_family1 + S_family2 - 12) mod 1234567891.
"""

from __future__ import annotations

import decimal
from decimal import Decimal


def solve(exp_pow: int = 10, mod: int = 1234567891) -> int:
    """Compute S(10^{10^{exp_pow}}) modulo mod in O(log(n_max)) time."""
    # 1. High-precision calculation of n_max for Family 1
    decimal.getcontext().prec = 60
    ln10 = Decimal(10).ln()
    ln_lambda = (Decimal(3) + Decimal(8).sqrt()).ln()
    ln_denom = (Decimal(8).sqrt()).ln()
    e_val = Decimal(10) ** exp_pow
    n_float = (e_val * ln10 + ln_denom) / ln_lambda
    k = int(n_float)

    # 2. Matrix exponentiation for Family 1: P_{k+1}, P_k
    def mat_mul(a_mat: list[list[int]], b_mat: list[list[int]]) -> list[list[int]]:
        return [
            [
                (a_mat[0][0] * b_mat[0][0] + a_mat[0][1] * b_mat[1][0]) % mod,
                (a_mat[0][0] * b_mat[0][1] + a_mat[0][1] * b_mat[1][1]) % mod,
            ],
            [
                (a_mat[1][0] * b_mat[0][0] + a_mat[1][1] * b_mat[1][0]) % mod,
                (a_mat[1][0] * b_mat[0][1] + a_mat[1][1] * b_mat[1][1]) % mod,
            ],
        ]

    def mat_pow(a_mat: list[list[int]], p: int) -> list[list[int]]:
        res = [[1, 0], [0, 1]]
        base = a_mat
        while p > 0:
            if p % 2 == 1:
                res = mat_mul(res, base)
            base = mat_mul(base, base)
            p //= 2
        return res

    t_mat = [[6, -1 % mod], [1, 0]]
    tk = mat_pow(t_mat, k - 1)
    p_k1 = (tk[0][0] * 12 + tk[0][1] * 2) % mod
    p_k = (tk[1][0] * 12 + tk[1][1] * 2) % mod
    s_case1 = ((p_k1 - p_k - 10) % mod * pow(4, mod - 2, mod)) % mod

    # 3. Family 2: sum of (4m^2 + 6m + 2) for m = 1..m_max
    # m_max = (10^(5 * 10^9) - 2) / 2 mod mod
    pow_exp = (5 * (10 ** (exp_pow - 1))) % (mod - 1)
    ten_pow = pow(10, pow_exp, mod)
    m_max = ((ten_pow - 2) % mod * pow(2, mod - 2, mod)) % mod

    # Closed-form sum: 2 m(m+1)(2m+1)/3 + 3 m(m+1) + 2m
    term1 = (
        2
        * m_max
        % mod
        * (m_max + 1)
        % mod
        * (2 * m_max + 1)
        % mod
        * pow(3, mod - 2, mod)
    ) % mod
    term2 = (3 * m_max % mod * (m_max + 1) % mod) % mod
    term3 = (2 * m_max) % mod
    s_case2 = (term1 + term2 + term3) % mod

    # Deduplicate (3, 4, 5) with perimeter 12
    return (s_case1 + s_case2 - 12) % mod


if __name__ == "__main__":
    print(solve())
