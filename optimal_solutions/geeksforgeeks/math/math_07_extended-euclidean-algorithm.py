"""Optimal solution for math_07: Extended Euclidean Algorithm.

Given two non-negative integers a and b (not both
"""


def solve(a, b):
    """Extended Euclidean: a*x + b*y = gcd(a, b)."""
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t
    return old_r, old_s, old_t
