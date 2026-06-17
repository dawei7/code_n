"""Solution for dp_21: Boolean Parenthesization.

Count the number of ways to parenthesize a boolean
expression (operands T/F, operators &|^) so it evaluates
to True. Interval DP: T[i][j] / F[i][j] = count of ways
for s[i..j]. At each split, combine the four quadrants
based on the operator.
Source: https://www.geeksforgeeks.org/boolean-parenthesization-problem/

Inputs passed to solve():
    s: expression string (operands T/F, operators & | ^).
    n: length of s.

Goal:
    the number of parenthesizations that evaluate to True.

Samples:
Sample 1 input:  s = "T|T&F^T", n = 7
Sample 1 output: 4

Sample 2 input:  s = "T^T^T", n = 5
Sample 2 output: 0


"""

def solve(s, n):
    # Write your code here.
    return None
