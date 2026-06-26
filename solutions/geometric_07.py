"""
Description
-----------
Given n points in the plane, find the maximum
            number of points that lie on the same straight line.
            For each pivot point, compute the slope to every
            other point (as a normalized (dy, dx) pair to avoid
            floating-point precision issues). Group points by
            slope and track the max group size. Handle vertical
            lines and duplicate points separately. O(n^2 log n)
            with the hash map, O(n^2) without.
            Source: https://www.geeksforgeeks.org/dsa/count-maximum-points-on-same-line/

Examples
--------
Example 1:
Input:  points = [(-1, 1), (0, 0), (1, 1), (2, 2), (3, 3), (3, 4)], n = 6
Output: 4 (the line y = x has 4 points)

Example 2:
Input:  points = [(0, 0), (1, 0), (0, 1), (1, 1)], n = 4
Output: 2 (no three collinear)
"""

def solve(points, n):
    # Write your code here.
    return None
