"""
Description
-----------
Given n points in the plane, return the smallest
            Euclidean distance between any two of them. The
            classic O(n log n) plane-sweep algorithm: split
            by the median x, recurse on each half, then check
            the strip of points within d of the cut. Brute
            force O(n^2) verify is fine for the small n we use.
            Source: https://www.geeksforgeeks.org/closest-pair-of-points-using-divide-and-conquer/

Examples
--------
Example 1:
Input:  points = [(0, 0), (5, 0), (3, 4)], n = 3
Output: 3.0 (between (0, 0) and (3, 4))

Example 2:
Input:  points = [(0, 0), (1, 1), (2, 2), (3, 3)], n = 4
Output: 1.4142135... (sqrt 2)
"""

def solve(points, n):
    # Write your code here.
    return None
