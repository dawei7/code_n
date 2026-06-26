"""Optimal solution for dc_10: Floor Square Root.

Given a non-negative integer n, return floor(sqrt(n)).
"""


def solve(n):
    """Return floor(sqrt(n)) via binary search (D&C style)."""
    if n < 2:
        return n
    lo, hi, res = 1, n, 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        sq = mid * mid
        if sq <= n:
            res = mid
            lo = mid + 1
        else:
            hi = mid - 1
    return res
