"""Optimal solution for recursion_01: Power Sum.

Recursive halving: x^n = (x^(n//2))^2, with an extra x when
n is odd. O(log n) time.
"""


def solve(x, n):
    if n == 0:
        return 1
    half = solve(x, n // 2)
    if n % 2 == 0:
        return half * half
    return x * half * half
