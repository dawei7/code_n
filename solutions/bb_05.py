"""Solution for bb_05: N-Queen (Branch and Bound).


            Place N queens on an N x N board so that no two
            queens attack each other. Use branch and bound:
            place queens column by column, and for each column
            prune any row that is already attacked (by row,
            or by either of the two diagonal directions). Use
            three boolean arrays for O(1) safety checks:
            row[r], slash[r + c] (for / diagonals), and
            backslash[c - r + (N-1)] (for backslash diagonals).
            Return a sorted list of (row, col) tuples for one
            valid placement, or an empty list if none exists
            for this N.
            Source: https://www.geeksforgeeks.org/dsa/n-queen-problem-using-branch-and-bound/
            

Inputs passed to solve():
    n: board size (small in tests, 1 <= n <= 8).

Goal:
    a list of (row, col) tuples for one valid N-queen placement, sorted by col; empty list if no solution exists.

Samples:
Sample 1 input:  n = 1
Sample 1 output: [(0, 0)]

Sample 2 input:  n = 4
Sample 2 output: [(1, 0), (3, 1), (0, 2), (2, 3)] (one valid placement)

Sample 3 input:  n = 8
Sample 3 output: a valid 8-queen placement, e.g. [(0,0),(4,1),(7,2),(5,3),(2,4),(6,5),(1,6),(3,7)]

"""

def solve(n):
    # Write your code here.
    return None
