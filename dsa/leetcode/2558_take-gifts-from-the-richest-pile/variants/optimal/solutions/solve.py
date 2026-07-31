import heapq
from math import isqrt


def solve(gifts: list[int], k: int) -> int:
    heap = [-gift for gift in gifts]
    heapq.heapify(heap)

    for _ in range(k):
        richest = -heapq.heappop(heap)
        heapq.heappush(heap, -isqrt(richest))

    return -sum(heap)
