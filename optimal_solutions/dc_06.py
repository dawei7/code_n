"""Optimal solution for dc_06: Strassen Matrix Multiplication.

Multiply two 2x2 matrices using Strassen's algorithm
"""


def solve(A, B, n):
    """Strassen 2x2 matrix multiplication.

    Seven products (p1..p7) replace the schoolbook eight,
    trading a few extra additions for one fewer multiply.
    """
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    if n == 2:
        a, b, c, d = A[0][0], A[0][1], A[1][0], A[1][1]
        e, f, g, h = B[0][0], B[0][1], B[1][0], B[1][1]
        p1 = a * (f - h)
        p2 = (a + b) * h
        p3 = (c + d) * e
        p4 = d * (g - e)
        p5 = (a + d) * (e + h)
        p6 = (b - d) * (g + h)
        p7 = (a - c) * (e + f)
        c00 = p5 + p4 - p2 + p6
        c01 = p1 + p2
        c10 = p3 + p4
        c11 = p1 + p5 - p3 - p7
        return [[c00, c01], [c10, c11]]
    return _naive(A, B, n)

def _naive(A, B, n):
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C
