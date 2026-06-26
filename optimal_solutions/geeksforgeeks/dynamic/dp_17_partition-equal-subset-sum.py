"""Optimal solution for dp_17: Partition Equal Subset Sum.

True iff arr can be split into two equal-sum subsets.
"""


def solve(arr):
    total = sum(arr)
    if total % 2 != 0:
        return False
    target = total // 2
    reachable = {0}
    for v in arr:
        reachable = reachable | {s + v for s in reachable}
    return target in reachable
