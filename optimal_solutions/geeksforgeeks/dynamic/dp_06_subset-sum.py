"""Optimal solution for dp_06: Subset Sum.

True iff some subset of arr sums to target. Set-based DP over
the running reachable sums.
"""


def solve(arr, target):
    reachable = {0}
    for v in arr:
        reachable = reachable | {s + v for s in reachable}
    return target in reachable
