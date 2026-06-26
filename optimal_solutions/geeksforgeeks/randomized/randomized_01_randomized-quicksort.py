"""Optimal solution for randomized_01: Randomized Quicksort.

Quicksort with a random pivot. Each partition picks a random
index in [lo, hi], swaps it to the end, then Lomuto-partitions.
Expected O(n log n); with adversarial input, expected
O(n log n) - the random pivot breaks the bad case.
"""


def solve(data, n):
    import random
    work = list(data)

    def partition(lo, hi):
        pivot_idx = random.randint(lo, hi)
        work[pivot_idx], work[hi] = work[hi], work[pivot_idx]
        pivot = work[hi]
        i = lo
        for j in range(lo, hi):
            if work[j] <= pivot:
                work[i], work[j] = work[j], work[i]
                i += 1
        work[i], work[hi] = work[hi], work[i]
        return i

    def sort(lo, hi):
        if lo < hi:
            p = partition(lo, hi)
            sort(lo, p - 1)
            sort(p + 1, hi)

    if n > 1:
        sort(0, n - 1)
    return work
