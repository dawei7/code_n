"""
Description
-----------
Compute the convex hull of n points using Jarvis
            March (gift wrapping). Start at the leftmost point,
            then repeatedly find the next hull vertex as the
            point that makes the smallest (most counterclockwise)
            angle with the current edge. Stop when we return
            to the start. Return the hull vertices as a list of
            (x, y) tuples in CCW order, starting from the
            leftmost point. O(n^2) worst case, but O(nh) for
            small hulls.
            Source: https://www.geeksforgeeks.org/dsa/convex-hull-using-jarvis-algorithm/

Examples
--------
Example 1:
Input:  points = [(0, 0), (1, 1), (2, 0), (1, 0.5), (0, 2)], n = 5
Output: a sorted CCW hull, e.g. [(0, 0), (2, 0), (0, 2)]
"""

def solve(points, n):
    # Write your code here.
    return None
