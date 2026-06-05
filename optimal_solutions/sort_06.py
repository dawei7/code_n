"""Optimal solution for sort_06: Heap Sort.

Auto-generated from challenges/algorithms/sorting.py:SPECS.
O(n log n) time.
"""


def solve(data, n):
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

    # Pop the root into the last position, one at a time.
    for end in range(n - 1, 0, -1):
        data[0], data[end] = data[end], data[0]
        sift_down(0, end)
    return data
