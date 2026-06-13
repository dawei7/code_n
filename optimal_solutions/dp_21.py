"""Optimal solution for dp_21: Boolean Parenthesization.

Count the number of ways to parenthesize a boolean
expression (operands T/F, operators &|^) so it evaluates
to True. Interval DP: T[i][j] / F[i][j] = count of ways
for s[i..j]. At each split, combine the four quadrants
based on the operator.
"""


def solve(s, n):
    if n == 0:
        return 0
    T = [[0] * n for _ in range(n)]
    F = [[0] * n for _ in range(n)]
    for i in range(0, n, 2):
        T[i][i] = 1 if s[i] == "T" else 0
        F[i][i] = 1 if s[i] == "F" else 0
    for gap in range(2, n, 2):
        for i in range(0, n - gap, 2):
            j = i + gap
            T[i][j] = F[i][j] = 0
            for k in range(i + 1, j, 2):
                op = s[k]
                lt, lf = T[i][k - 1], F[i][k - 1]
                rt, rf = T[k + 1][j], F[k + 1][j]
                if op == "&":
                    T[i][j] += lt * rt
                    F[i][j] += lt * rf + lf * rt + lf * rf
                elif op == "|":
                    T[i][j] += lt * rt + lt * rf + lf * rt
                    F[i][j] += lf * rf
                else:  # ^
                    T[i][j] += lt * rf + lf * rt
                    F[i][j] += lt * rt + lf * rf
    return T[0][n - 1]
