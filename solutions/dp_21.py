"""
Description
-----------
Count the number of ways to parenthesize a boolean
expression (operands T/F, operators &|^) so it evaluates
to True. Interval DP: T[i][j] / F[i][j] = count of ways
for s[i..j]. At each split, combine the four quadrants
based on the operator.
Source: https://www.geeksforgeeks.org/boolean-parenthesization-problem/

Examples
--------
Example 1:
Input:  s = "T|T&F^T", n = 7
Output: 4

Example 2:
Input:  s = "T^T^T", n = 5
Output: 0
"""

def solve(s, n):
    # Write your code here.
    return None
