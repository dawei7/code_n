"""
Description
-----------
Build a 2D Binary Indexed Tree on an n x n matrix,
            apply a sequence of point updates (add delta to a
            cell), then answer each sub-matrix sum query
            sum over the rectangle (r1, c1) .. (r2, c2)
            inclusive, using inclusion-exclusion over four
            2D prefix sums. O(log^2 n) per update and per
            query.
            Source: https://www.geeksforgeeks.org/dsa/two-dimensional-binary-indexed-tree-or-fenwick-tree/

Examples
--------
Example 1:
Input:  matrix = [[1, 2, 3, 4], [5, 3, 8, 1], [4, 6, 7, 5], [2, 4, 8, 9]], n = 4, updates = [], queries = [(1, 1, 3, 2)], q = 1
Output: [30]

Example 2:
Input:  matrix = [[1, 2, 3, 4], [5, 3, 8, 1], [4, 6, 7, 5], [2, 4, 8, 9]], n = 4, updates = [(0, 0, 1), (1, 1, -1)], queries = [(0, 0, 3, 3)], q = 1
Output: [51] ( = 55 + 1 - 5)
"""

def solve(matrix, n, updates, queries, q):
    # Write your code here.
    return None
