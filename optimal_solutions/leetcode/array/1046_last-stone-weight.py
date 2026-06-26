"""Optimal solution for LeetCode 1046: Last Stone Weight."""

from heapq import heapify, heappop, heappush


def solve(stones: list[int]) -> int:
    heap = [-stone for stone in stones]
    heapify(heap)
    while len(heap) > 1:
        first = -heappop(heap)
        second = -heappop(heap)
        if first != second:
            heappush(heap, -(first - second))
    return -heap[0] if heap else 0
