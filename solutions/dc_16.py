"""
Description
-----------
Given n points in the plane, return the vertices of
            the convex hull as a set of (x, y) tuples. Quickhull
            is a D&C analogue of quicksort: split by the line
            through the leftmost and rightmost points, recurse
            on each side using the farthest point from the line
            as the new pivot, and discard everything inside the
            resulting triangle. Average O(n log n), worst O(n^2).
            The canonical O(n log n) verify uses Andrew's
            monotone chain so the test stays accurate for all
            inputs.
            Source: https://www.geeksforgeeks.org/dsa/quickhull-algorithm-convex-hull/

Examples
--------
Example 1:
Input:  points = [(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)], n = 8
Output: a set like {(0, 0), (0, 3), (1, 1), (3, 1), (4, 4)} (any valid hull accepted)

Example 2:
Input:  points = [(0, 0), (0, 4), (-4, 0), (5, 0), (0, -6), (1, 0)], n = 6
Output: a set like {(-4, 0), (5, 0), (0, -6), (0, 4)} (any valid hull accepted)
"""

def solve(points, n):
    # Write your code here.
    return None
