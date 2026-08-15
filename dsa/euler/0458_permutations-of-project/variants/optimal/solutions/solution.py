"""Project Euler Problem 458: Permutations of Project.

Find T(10^12) mod 10^9, where T(n) is the number of strings of length n
formed by the 7 letters of 'project' with no 7-character permutation substring.
"""

from typing import List

MOD = 1_000_000_000


def _mat_mul(
    a_mat: List[List[int]], b_mat: List[List[int]], mod: int = MOD
) -> List[List[int]]:
    dim = len(a_mat)
    c_mat = [[0] * dim for _ in range(dim)]
    for i in range(dim):
        for k in range(dim):
            if a_mat[i][k] == 0:
                continue
            for j in range(dim):
                c_mat[i][j] = (c_mat[i][j] + a_mat[i][k] * b_mat[k][j]) % mod
    return c_mat


def _mat_pow(
    a_mat: List[List[int]], exp: int, mod: int = MOD
) -> List[List[int]]:
    dim = len(a_mat)
    res = [[int(i == j) for j in range(dim)] for i in range(dim)]
    base = [row[:] for row in a_mat]
    while exp > 0:
        if exp & 1:
            res = _mat_mul(res, base, mod)
        base = _mat_mul(base, base, mod)
        exp >>= 1
    return res


def solve(n: int = 10**12, mod: int = MOD) -> int:
    """Compute T(n) mod mod using 7-state distinct-suffix transition matrix binary exponentiation."""
    mat = [[0] * 7 for _ in range(7)]
    mat[0][1] = 7
    for k in range(1, 7):
        for j in range(1, k + 1):
            mat[k][j] = 1
        if k + 1 < 7:
            mat[k][k + 1] = 7 - k

    mat_n = _mat_pow(mat, n, mod)
    return sum(mat_n[0][j] for j in range(7)) % mod


if __name__ == "__main__":
    print(solve())
