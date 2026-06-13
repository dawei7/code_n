"""Optimal solution for dc_03: Kth Smallest (Quickselect).

Quickselect: partition the array around a pivot (Lomuto-style),
then only recurse into the half that contains the kth smallest.
O(n) average case, O(n^2) worst case on pathological data.
The setup shuffles the array first to keep the worst case rare.
"""


def solve(arr, k, n):
    if k < 1 or k > n:
        return -1
    work = list(arr)
    target = k - 1  # 0-indexed

    def select(lo, hi):
        if lo == hi:
            return work[lo]
        pivot = work[hi]
        i = lo
        for j in range(lo, hi):
            if work[j] <= pivot:
                work[i], work[j] = work[j], work[i]
                i += 1
        work[i], work[hi] = work[hi], work[i]
        if i == target:
            return work[i]
        if i < target:
            return select(i + 1, hi)
        return select(lo, i - 1)

    return select(0, n - 1)
