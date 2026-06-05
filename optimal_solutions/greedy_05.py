"""Optimal solution for greedy_05: Optimal Merge Pattern.

Auto-generated from challenges/algorithms/greedy.py:SPECS.
O(n log n) time.
"""


def solve(sizes, n):
    import heapq
    if n <= 1:
        return 0
    heap = list(sizes)
    heapq.heapify(heap)
    total = 0
    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        merged = a + b
        total += merged
        heapq.heappush(heap, merged)
    return total
