"""Solution for dc_10: Floor Square Root.


            Given a non-negative integer n, return floor(sqrt(n)).
            If n is a perfect square return the exact root; otherwise
            return the largest integer whose square is <= n.
            Binary search on the range [1, n] (D&C: keep the half
            whose square is still <= n, discard the rest).
            Source: https://www.geeksforgeeks.org/dsa/square-root-of-an-integer/
            

Inputs passed to solve():
    n: non-negative integer to take the floor square root of.

Goal:
    the floor of sqrt(n) as a non-negative int.

Samples:
Sample 1 input:  n = 0
Sample 1 output: 0

Sample 2 input:  n = 1
Sample 2 output: 1

Sample 3 input:  n = 4
Sample 3 output: 2
Sample 4 input:  n = 11
Sample 4 output: 3
Sample 5 input:  n = 16
Sample 5 output: 4

"""

def solve(n):
    # Write your code here.
    return None
