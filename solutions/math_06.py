"""
Description
-----------
The Carmichael function lambda(n): the smallest m > 0
such that a^m == 1 (mod n) for every a coprime to n.
Compute via prime factorization: lambda(p^k) is p^(k-1)
* (p-1) for odd primes, 2^(k-2) for n = 2^k, k >= 3.
For composite n, lambda is the lcm of the per-prime-power
lambdas.
Source: https://www.geeksforgeeks.org/carmichael-function/

Examples
--------
Example 1:
Input:  n = 12
Output: 2 (gcd(5, 12) = 1, 5^2 = 25 = 1 mod 12)

Example 2:
Input:  n = 35
Output: 12 (lambda(5) = 4, lambda(7) = 6, lcm = 12)
"""

def solve(n):
    # Write your code here.
    return None
