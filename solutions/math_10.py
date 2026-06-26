"""
Description
-----------
Given a positive integer n, return phi(n): the
            number of integers in [1, n] coprime to n. Two
            approaches: (1) factorize n; phi is multiplicative
            and phi(p^k) = p^k - p^(k-1) = p^(k-1) * (p-1),
            so phi(n) = n * product over distinct prime p|n
            of (1 - 1/p). (2) Euler's sieve: for n up to N,
            compute all phi in O(N log log N). We use the
            factorization approach (n is small). O(sqrt(n)) time.
            Source: https://www.geeksforgeeks.org/eulers-totient-function/

Examples
--------
Example 1:
Input:  n_val = 1
Output: 1 (gcd(1, 1) = 1, just the element 1)

Example 2:
Input:  n_val = 10
Output: 4 (1, 3, 7, 9 are coprime to 10)

Example 3:
Input:  n_val = 36
Output: 12
"""

def solve(n_val):
    # Write your code here.
    return None
