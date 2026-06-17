"""Solution for dc_12: Tiling Problem (2 x N board).


            Given a 2 x n board and tiles of size 2 x 1, count
            the number of ways to tile the whole board. The
            classic recurrence is T(n) = T(n-1) + T(n-2) --
            place a vertical tile (T(n-1) cases) or two
            horizontal tiles (T(n-2) cases). Implemented with
            an O(n) DP scan; the D&C view is via matrix
            exponentiation in O(log n), but the operation
            budget we measure is the simple linear walk.
            Source: https://www.geeksforgeeks.org/dsa/tiling-problem-using-divide-and-conquer-algorithm/
            

Inputs passed to solve():
    n: board length (n >= 0).

Goal:
    the number of ways to tile a 2 x n board with 2 x 1 dominoes, as a non-negative int.

Samples:
Sample 1 input:  n = 0
Sample 1 output: 1

Sample 2 input:  n = 1
Sample 2 output: 1

Sample 3 input:  n = 2
Sample 3 output: 2
Sample 4 input:  n = 3
Sample 4 output: 3
Sample 5 input:  n = 4
Sample 5 output: 5

"""

def solve(n):
    # Write your code here.
    return None
