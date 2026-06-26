"""
Description
-----------
Return True iff two line segments intersect. The standard
orientation test: the segments straddle each other iff
the orientations of (p1, q1, p2) and (p1, q1, q2) have
opposite signs, AND the orientations of (p2, q2, p1)
and (p2, q2, q1) have opposite signs. Plus the collinear-
on-segment edge cases.
Source: https://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/

Examples
--------
Example 1:
Input:  seg1 = ((1, 1), (10, 1)), seg2 = ((1, 2), (10, 2))
Output: False (parallel)

Example 2:
Input:  seg1 = ((0, 0), (10, 10)), seg2 = ((0, 10), (10, 0))
Output: True (cross at (5, 5))
"""

def solve(seg1, seg2):
    # Write your code here.
    return None
