"""Project Euler Problem 382: Generating Polygons.

Find the last 9 digits of f(10^18), where f(n) is the number of subsets of {s_1, ..., s_n}
that generate at least one polygon.
"""

from typing import List


def solve(n: int = 10**18, mod: int = 10**9) -> str:
    """Compute the last 9 digits of f(n) using 12x12 matrix exponentiation."""
    dim = 12

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

    # Build transition matrix M of size 12x12
    # State: [b_i, b_{i-1}, ..., b_{i-5}, 2^i, 2^{i-1}, ..., 2^{i-3}, S_i, 1]^T
    mat_m = [[0] * dim for _ in range(dim)]

    # Row 0: b_{i+1} = 2*b_{i-2} + b_{i-3} - b_{i-5} + 5*2^{i-3} + 1
    mat_m[0][2] = 2 % mod
    mat_m[0][3] = 1
    mat_m[0][5] = mod - 1
    mat_m[0][9] = 5
    mat_m[0][11] = 1

    # Shift b's
    mat_m[1][0] = 1
    mat_m[2][1] = 1
    mat_m[3][2] = 1
    mat_m[4][3] = 1
    mat_m[5][4] = 1

    # Powers of two
    mat_m[6][6] = 2
    mat_m[7][6] = 1
    mat_m[8][7] = 1
    mat_m[9][8] = 1

    # Prefix sum S_{i+1} = S_i + b_{i+1}
    mat_m[10][10] = 1
    for j in range(dim):
        mat_m[10][j] = (mat_m[10][j] + mat_m[0][j]) % mod

    mat_m[11][11] = 1

    # Dynamically compute initial sequence s and initial base counts b_0..b_5
    seq_s = [0, 1, 2, 3]
    for _ in range(4, 10):
        seq_s.append(seq_s[-1] + seq_s[-3])

    b_init: List[int] = []
    for i in range(6):
        elements = seq_s[1 : i + 1]
        count = 0
        for mask in range(1 << i):
            tot = sum(elements[bit] for bit in range(i) if (mask & (1 << bit)))
            if tot <= seq_s[i + 1]:
                count += 1
        b_init.append(count)

    idx = n - 1
    if idx <= 5:
        prefix_s = sum(b_init[: idx + 1]) % mod
    else:
        s5 = sum(b_init) % mod
        v_init = [
            b_init[5],
            b_init[4],
            b_init[3],
            b_init[2],
            b_init[1],
            b_init[0],
            pow(2, 5, mod),
            pow(2, 4, mod),
            pow(2, 3, mod),
            pow(2, 2, mod),
            s5,
            1,
        ]
        mat_p = mat_pow(mat_m, idx - 5)
        prefix_s = sum(mat_p[10][j] * v_init[j] for j in range(dim)) % mod

    ans = (pow(2, n, mod) - 1 - prefix_s) % mod
    return f"{ans:09d}"


if __name__ == "__main__":
    print(solve())
