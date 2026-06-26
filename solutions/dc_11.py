"""
Description
-----------
Compute (x  n) % m for non-negative integers x, n
            and a positive modulus m. Naive multiplication of x
            by itself n times takes O(n) steps and overflows for
            big n. The D&C trick: square-and-reduce the base
            while halving the exponent. Reduces O(n) to O(log n).
            Source: https://www.geeksforgeeks.org/dsa/modular-exponentiation-power-in-modular-arithmetic/

Examples
--------
Example 1:
Input:  x = 3, n = 2, m = 4
Output: 1

Example 2:
Input:  x = 2, n = 6, m = 10
Output: 4

Example 3:
Input:  x = 7, n = 0, m = 13
Output: 1

Example 4:
Input:  x = 0, n = 5, m = 7
Output: 0
"""

def solve(x, n, m):
    # Write your code here.
    return None
