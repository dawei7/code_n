"""Optimal solution for LeetCode 1054: Distant Barcodes."""

from collections import Counter
from heapq import heappop, heappush


def solve(barcodes: list[int]) -> list[int]:
    heap = [(-count, value) for value, count in Counter(barcodes).items()]
    result: list[int] = []
    import heapq

    heapq.heapify(heap)
    previous_count = 0
    previous_value = 0
    while heap:
        count, value = heappop(heap)
        result.append(value)
        if previous_count < 0:
            heappush(heap, (previous_count, previous_value))
        previous_count = count + 1
        previous_value = value
    return result
