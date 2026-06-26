"""Optimal solution for greedy_11: Egyptian Fraction.

Every positive rational number ``p/q`` can be written as the sum
of distinct unit fractions (1/d). The greedy algorithm picks the
smallest unit fraction not smaller than the remainder, which is
``1 / ceil(q / p)``. Stop when the remainder hits zero; cap the
loop at q+1 steps so a degenerate input can't run forever.
"""


def solve(p, q):
    if p <= 0 or q <= 0:
        return []
    result = []
    for _ in range(q + 1):
        if p == 0:
            break
        d = (q + p - 1) // p  # ceil(q / p)
        result.append(d)
        p = p * d - q
        q = q * d
        # Reduce to keep numbers small.
        from math import gcd
        g = gcd(p, q) or 1
        p //= g
        q //= g
    return result
