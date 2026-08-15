"""Project Euler Problem 435: Polynomials of Fibonacci Numbers.

Find sum_{x=0..100} F_n(x) mod 15!, where F_n(x) = sum_{i=0..n} f_i * x^i and n = 10^15.
"""

from math import factorial
from typing import List

MOD = factorial(15)


def _mat_mul(
    a: List[List[int]], b: List[List[int]], mod: int = MOD
) -> List[List[int]]:
    c = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for k in range(3):
            if a[i][k] == 0:
                continue
            for j in range(3):
                c[i][j] = (c[i][j] + a[i][k] * b[k][j]) % mod
    return c


def _mat_pow(
    m: List[List[int]], p: int, mod: int = MOD
) -> List[List[int]]:
    res = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    base = m
    while p > 0:
        if p & 1:
            res = _mat_mul(res, base, mod)
        base = _mat_mul(base, base, mod)
        p >>= 1
    return res


def _eval_f_n(n: int, x: int, mod: int = MOD) -> int:
    if n == 0 or x == 0:
        return 0
    m_mat = [
        [1, 1, 0],
        [0, x % mod, (x * x) % mod],
        [0, 1, 0],
    ]
    m_n = _mat_pow(m_mat, n, mod)
    return (m_n[0][1] * x) % mod


def solve(n: int = 10**15, max_x: int = 100, mod: int = MOD) -> int:
    """Compute sum_{x=0..max_x} F_n(x) mod mod using 3x3 matrix exponentiation."""
    total = 0
    for x in range(max_x + 1):
        total = (total + _eval_f_n(n, x, mod)) % mod
    return total


if __name__ == "__main__":
    print(solve())
