"""Optimal solution for approx_06: Bin Packing (First-Fit Decreasing).

Given a list of item sizes in (0, 1] and unit-
"""


def solve(sizes, n):
    """First-Fit Decreasing bin packing."""
    if n == 0:
        return 0
    # Sort items by size descending.
    items = sorted(sizes, reverse=True)
    bins = []  # each entry is the remaining capacity of a bin
    for s in items:
        placed = False
        for i in range(len(bins)):
            if bins[i] >= s:
                bins[i] -= s
                placed = True
                break
        if not placed:
            bins.append(1.0 - s)
    return len(bins)
