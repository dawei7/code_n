"""
Description
-----------
Given a and m (with gcd(a, m) = 1), find x such
            that a*x = 1 (mod m). The inverse exists iff a and
            m are coprime. Use the extended Euclidean algorithm:
            the coefficient of a in a*x + m*y = gcd(a, m) = 1
            is the inverse (mod m). If gcd != 1, return 0 as a
            sentinel for 'no inverse'. O(log min(a, m)) time.
            Source: https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/

Examples
--------
Example 1:
Input:  a = 3, m = 11
Output: 4 since 3*4 = 12 = 1 (mod 11)

Example 2:
Input:  a = 10, m = 17
Output: 12 since 10*12 = 120 = 1 (mod 17) (10^-1 = 12)
"""

def solve(a, m):
    # Write your code here.
    return None
