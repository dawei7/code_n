"""Project Euler Problem 434: Rigid Graphs.

Find S(100) mod 1000000033, where S(N) is the sum of R(i, j) for 1 <= i, j <= N,
and R(m, n) is the number of ways to make the m x n grid graph rigid.
"""

from typing import List

MOD = 1_000_000_033


def solve(n_limit: int = 100) -> int:
    """Compute S(n_limit) mod MOD using connected bipartite graph component dynamic programming."""
    comb = [[0] * (n_limit + 1) for _ in range(n_limit + 1)]
    for i in range(n_limit + 1):
        comb[i][0] = 1
        for j in range(1, i + 1):
            comb[i][j] = (comb[i - 1][j - 1] + comb[i - 1][j]) % MOD

    pow2 = [1] * (n_limit * n_limit + 1)
    for i in range(1, n_limit * n_limit + 1):
        pow2[i] = (pow2[i - 1] * 2) % MOD

    c_mat: List[List[int]] = [
        [0] * (n_limit + 1) for _ in range(n_limit + 1)
    ]
    c_mat[1][0] = 1
    c_mat[0][1] = 1

    for m in range(1, n_limit + 1):
        for n in range(1, n_limit + 1):
            sub_sum = 0
            for i in range(1, m + 1):
                c_m = comb[m - 1][i - 1]
                for j in range(0, n + 1):
                    if i == m and j == n:
                        continue
                    if c_mat[i][j] == 0:
                        continue
                    term = (c_m * comb[n][j]) % MOD
                    term = (term * c_mat[i][j]) % MOD
                    term = (term * pow2[(m - i) * (n - j)]) % MOD
                    sub_sum = (sub_sum + term) % MOD
            c_mat[m][n] = (pow2[m * n] - sub_sum) % MOD

    total_sum = 0
    for i in range(1, n_limit + 1):
        for j in range(1, n_limit + 1):
            total_sum = (total_sum + c_mat[i][j]) % MOD

    return total_sum


if __name__ == "__main__":
    print(solve())
