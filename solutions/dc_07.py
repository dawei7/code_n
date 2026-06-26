"""
Description
-----------
Given n axis-aligned rectangular buildings as
            (left, height, right) triples, return the skyline
            as a list of (x, height) key points. A key point is
            a position where the height changes. Consecutive
            points with the same height are collapsed.
            D&C: recursively get the left and right skylines
            and merge them in O(n). The setup keeps n small
            so an O(n^2) verify is fast.
            Source: https://www.geeksforgeeks.org/divide-and-conquer-set-7-the-skyline-problem/

Examples
--------
Example 1:
Input:  buildings = [(1, 4, 5), (2, 3, 7), (4, 2, 9)], n = 3
Output: [[1, 4], [4, 3], [5, 2], [7, 0], [9, 0]]

Example 2:
Input:  buildings = [(0, 3, 5)], n = 1
Output: [[0, 3], [5, 0]]
"""

def solve(buildings, n):
    # Write your code here.
    return None
