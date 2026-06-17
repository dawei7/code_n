"""Solution for math_06: Carmichael Function.

The Carmichael function lambda(n): the smallest m > 0
such that a^m == 1 (mod n) for every a coprime to n.
Compute via prime factorization: lambda(p^k) is p^(k-1)
* (p-1) for odd primes, 2^(k-2) for n = 2^k, k >= 3.
For composite n, lambda is the lcm of the per-prime-power
lambdas.
Source: https://www.geeksforgeeks.org/carmichael-function/

Inputs passed to solve():
    n: positive integer (small, with multiple prime factors in the setup).

Goal:
    the Carmichael function value lambda(n).

Samples:
Sample 1 input:  n = 12
Sample 1 output: 2 (gcd(5,12)=1, 5^2 = 25 = 1 mod 12)

Sample 2 input:  n = 35
Sample 2 output: 12 (lambda(5)=4, lambda(7)=6, lcm=12)


"""

def solve(n):
    # Write your code here.
    return None
