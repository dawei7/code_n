"""Project Euler Problem 377: Sum of Digits - Experience #13.

Find sum_{i=1..17} f(13^i) mod 10^9, where f(n) is the sum of all positive integers without zeros
whose digits sum to n.
"""

from typing import List


def solve(max_exp: int = 17, mod: int = 10**9) -> str:
    """Compute sum_{i=1..max_exp} f(13^i) mod mod via 18x18 matrix exponentiation."""
    dim = 18

    # Build transition matrix T of size 18x18
    # State: [f(n), f(n-1), ..., f(n-8), C(n), C(n-1), ..., C(n-8)]^T
    mat_t = [[0] * dim for _ in range(dim)]

    # Row 0: f(n+1) = 10 * sum_{d=1..9} f(n+1-d) + sum_{d=1..9} d * C(n+1-d)
    for d in range(1, 10):
        mat_t[0][d - 1] = 10
        mat_t[0][9 + d - 1] = d

    # Rows 1..8: shift f
    for k in range(1, 9):
        mat_t[k][k - 1] = 1

    # Row 9: C(n+1) = sum_{d=1..9} C(n+1-d)
    for d in range(1, 10):
        mat_t[9][9 + d - 1] = 1

    # Rows 10..17: shift C
    for k in range(1, 9):
        mat_t[9 + k][9 + k - 1] = 1

    def mat_mul(mat_a: List[List[int]], mat_b: List[List[int]]) -> List[List[int]]:
        mat_c = [[0] * dim for _ in range(dim)]
        for i in range(dim):
            for k in range(dim):
                if mat_a[i][k]:
                    for j in range(dim):
                        mat_c[i][j] = (
                            mat_c[i][j] + mat_a[i][k] * mat_b[k][j]
                        ) % mod
        return mat_c

    def mat_pow(mat_base: List[List[int]], power: int) -> List[List[int]]:
        res = [[1 if i == j else 0 for j in range(dim)] for i in range(dim)]
        curr_b = mat_base
        while power > 0:
            if power & 1:
                res = mat_mul(res, curr_b)
            curr_b = mat_mul(curr_b, curr_b)
            power >>= 1
        return res

    # Base vector at n = 1: f(1) = 1, C(1) = 1, C(0) = 1
    v1 = [0] * dim
    v1[0] = 1
    v1[9] = 1
    v1[10] = 1

    def compute_f(n_val: int) -> int:
        if n_val == 0:
            return 0
        if n_val == 1:
            return 1
        mat_pow_n = mat_pow(mat_t, n_val - 1)
        return sum(mat_pow_n[0][j] * v1[j] for j in range(dim)) % mod

    total_sum = 0
    for i in range(1, max_exp + 1):
        total_sum = (total_sum + compute_f(13**i)) % mod

    return f"{total_sum:09d}"


if __name__ == "__main__":
    print(solve())
