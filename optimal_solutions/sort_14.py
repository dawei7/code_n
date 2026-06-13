"""Optimal solution for sort_14: Intro Sort (Simplified).

Quicksort with depth limit; fall back to heapsort.
"""


def solve(data, n):
    if n <= 1:
        return data
    import math
    work = list(data)
    depth_limit = 2 * int(math.log2(n)) if n > 1 else 0

    def sift_down(lo, hi, root):
        while True:
            child = 2 * (root - lo) + 1 + lo
            if child >= hi:
                break
            if child + 1 < hi and work[child + 1] > work[child]:
                child += 1
            if work[child] > work[root]:
                work[root], work[child] = work[child], work[root]
                root = child
            else:
                break

    def heap_sort(lo, hi):
        for start in range((hi - lo) // 2 - 1 + lo, lo - 1, -1):
            sift_down(lo, hi, start)
        for end in range(hi - 1, lo, -1):
            work[lo], work[end] = work[end], work[lo]
            sift_down(lo, end, lo)

    def partition(lo, hi):
        pivot = work[hi]
        i = lo
        for j in range(lo, hi):
            if work[j] <= pivot:
                work[i], work[j] = work[j], work[i]
                i += 1
        work[i], work[hi] = work[hi], work[i]
        return i

    def intro_sort(lo, hi, depth):
        if hi - lo <= 1:
            return
        if depth == 0:
            heap_sort(lo, hi)
            return
        p = partition(lo, hi)
        intro_sort(lo, p, depth - 1)
        intro_sort(p + 1, hi, depth - 1)

    intro_sort(0, n, depth_limit)
    return work
