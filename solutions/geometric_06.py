"""
Description
-----------
Given two axis-aligned rectangles (each given by its
            top-left corner l1, l2 and bottom-right corner r1,
            r2 with l.x <= r.x and l.y >= r.y, i.e., y grows
            upward), determine whether the two rectangles
            overlap (have a positive-area intersection).
            Two rectangles do NOT overlap iff one is entirely
            to the left of the other, or entirely above the
            other. Return True if they overlap, False
            otherwise. O(1).
            Source: https://www.geeksforgeeks.org/dsa/find-two-rectangles-overlap/

Examples
--------
Example 1:
Input:  l1 = (0, 10), r1 = (10, 0), l2 = (5, 5), r2 = (15, 0)
Output: True (overlap)

Example 2:
Input:  l1 = (0, 10), r1 = (10, 0), l2 = (-10, 5), r2 = (-1, 0)
Output: False (rect2 is left of rect1)
"""

def solve(l1, r1, l2, r2):
    # Write your code here.
    return None
