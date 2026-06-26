"""
Description
-----------
Given a 2 x n board and tiles of size 2 x 1, count
            the number of ways to tile the whole board. The
            classic recurrence is T(n) = T(n-1) + T(n-2) --
            place a vertical tile (T(n-1) cases) or two
            horizontal tiles (T(n-2) cases). Implemented with
            an O(n) DP scan; the D&C view is via matrix
            exponentiation in O(log n), but the operation
            budget we measure is the simple linear walk.
            Source: https://www.geeksforgeeks.org/dsa/tiling-problem-using-divide-and-conquer-algorithm/

Examples
--------
Example 1:
Input:  n = 0
Output: 1

Example 2:
Input:  n = 1
Output: 1

Example 3:
Input:  n = 2
Output: 2

Example 4:
Input:  n = 3
Output: 3

Example 5:
Input:  n = 4
Output: 5
"""

def solve(n):
    # Write your code here.
    return None
