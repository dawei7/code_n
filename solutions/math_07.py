"""
Description
-----------
Given two non-negative integers a and b (not both
            zero), find integers x and y such that a*x + b*y
            = gcd(a, b). Run Euclid's algorithm but keep the
            coefficients at each step: when (a, b) -> (b, a%b),
            the new x = old_y - (a//b) * old_x, and the new y
            = old_x. Return (gcd, x, y). O(log min(a, b)) time.
            Foundation for the modular inverse.
            Source: https://www.geeksforgeeks.org/euclidean-algorithms-basic-and-extended/

Examples
--------
Example 1:
Input:  a = 35, b = 15
Output: (5, 1, -2) since 35*1 + 15*(-2) = 5 = gcd(35, 15)

Example 2:
Input:  a = 30, b = 20
Output: (10, 1, -1)
"""

def solve(a, b):
    # Write your code here.
    return None
