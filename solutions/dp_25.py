"""Solution for dp_25: Matrix Chain Multiplication.

Given n matrices with chain-compatible dimensions,
find the parenthesization that minimizes the total
number of scalar multiplications. Standard O(n^3) DP:
m[i][j] = min over k of m[i][k] + m[k+1][j] + cost of
the resulting multiplication.
Source: https://www.geeksforgeeks.org/matrix-chain-multiplication-dp-8/

Inputs passed to solve():
    dims: list of n (rows, cols) tuples; dims[i][1] == dims[i+1][0].
    n: number of matrices.

Goal:
    the minimum number of scalar multiplications.

Samples:
Sample 1 input:  dims = [(40, 20), (20, 30), (30, 10), (10, 30)], n = 4
Sample 1 output: 26000


"""

def solve(dims, n):
    # Write your code here.
    return None
