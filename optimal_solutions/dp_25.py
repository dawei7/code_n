"""Optimal solution for dp_25: Matrix Chain Multiplication.

m[i][j] = min over k of m[i][k] + m[k+1][j] +
dims[i][0] * dims[k][1] * dims[j][1].
"""


def solve(dims, n):
    if n <= 1:
        return 0
    INF = float("inf")
    m = [[0] * n for _ in range(n)]
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            m[i][j] = INF
            for k in range(i, j):
                cost = m[i][k] + m[k + 1][j] + dims[i][0] * dims[k][1] * dims[j][1]
                if cost < m[i][j]:
                    m[i][j] = cost
    return m[0][n - 1]
