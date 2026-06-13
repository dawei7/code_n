"""Optimal solution for heap_01: Build Max Heap.

Treat the input as a 0-indexed binary heap and sift-down from
the last non-leaf to the root. Bottom-up heapify is O(n) - faster
than the O(n log n) naive "insert" approach.
"""


def solve(data, n):
    # Sift down ``start`` in [0, n).
    def sift_down(start, end):
        root = start
        while True:
            child = 2 * root + 1
            if child >= end:
                break
            if child + 1 < end and data[child + 1] > data[child]:
                child += 1
            if data[child] > data[root]:
                data[root], data[child] = data[child], data[root]
                root = child
            else:
                break
    # Build the max-heap.
    for start in range(n // 2 - 1, -1, -1):
        sift_down(start, n)
    return data
