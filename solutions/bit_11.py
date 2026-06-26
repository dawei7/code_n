"""
Description
-----------
Given two non-negative integers left and right
with left <= right, return the bitwise AND of all
integers in the inclusive range [left, right].
The result is the common prefix (most significant
bits) of left and right, shifted into place. To
find it: keep clearing the lowest differing bit of
left while left > right; that's the common prefix.
Source: https://www.geeksforgeeks.org/bitwise-and-of-numbers-range/

Examples
--------
Example 1:
Input:  left = 5, right = 7
Output: 4 (binary 101 AND 110 AND 111 = 100)

Example 2:
Input:  left = 0, right = 0
Output: 0

Example 3:
Input:  left = 1, right = 1
Output: 1

Example 4:
Input:  left = 12, right = 15
Output: 12 (all 1100..1111 share 1100)
"""

def solve(left, right):
    # Write your code here.
    return None
