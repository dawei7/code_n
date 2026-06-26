"""Optimal solution for math_01: GCD (Euclidean algorithm).

Repeatedly replace (a, b) with (b, a mod b) until b is 0; the
last non-zero a is the gcd. O(log min(a, b)) time.
"""


def solve(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a
