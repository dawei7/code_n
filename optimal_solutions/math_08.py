"""Optimal solution for math_08: Modular Multiplicative Inverse.

Given a and m (with gcd(a, m) = 1), find x such
"""


def solve(a, m):
    """Return a^-1 mod m using extended Euclidean."""
    if m == 1:
        return 0
    # Reduce a mod m first.
    a = a % m
    if a == 0:
        return 0  # no inverse
    # Extended gcd of (a, m).
    old_r, r = a, m
    old_s, s = 1, 0
    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
    # old_r = gcd(a, m); old_s is the coefficient of a.
    if old_r != 1:
        return 0  # no inverse
    # Normalize to [0, m).
    return old_s % m
