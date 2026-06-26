"""
Description
-----------
Given n matrices with chain-compatible dimensions,
find the parenthesization that minimizes the total
number of scalar multiplications. Standard O(n^3) DP:
m[i][j] = min over k of m[i][k] + m[k+1][j] + cost of
the resulting multiplication.
Source: https://www.geeksforgeeks.org/matrix-chain-multiplication-dp-8/

Examples
--------
Example 1:
Input:  dims = [(40, 20), (20, 30), (30, 10), (10, 30)], n = 4
Output: 26000
"""

def solve(dims, n):
    # Write your code here.
    return None
