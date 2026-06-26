"""
Description
-----------
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

Examples
--------
Example 1:
Input:  n = 1
Output: [(0, 0)]

Example 2:
Input:  n = 4
Output: [(1, 0), (3, 1), (0, 2), (2, 3)] (one valid placement)

Example 3:
Input:  n = 8
Output: a valid 8-queen placement, e.g. [(0, 0), (4, 1), (7, 2), (5, 3), (2, 4), (6, 5), (1, 6), (3, 7)]
"""

def solve(n):
    # Write your code here.
    return None
