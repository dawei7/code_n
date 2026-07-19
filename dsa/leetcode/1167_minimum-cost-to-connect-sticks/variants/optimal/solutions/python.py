"""Optimal app-local solution for LeetCode 1167."""

from heapq import heapify, heappop, heappush


def solve(sticks: list[int]) -> int:
    heap = list(sticks)
    heapify(heap)
    total = 0
    while len(heap) > 1:
        combined = heappop(heap) + heappop(heap)
        total += combined
        heappush(heap, combined)
    return total
