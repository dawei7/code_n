"""Optimal solution for greedy_03: Huffman Coding.

Auto-generated from challenges/algorithms/greedy.py:SPECS.
O(n log n) time.
"""


def solve(chars, freq, n):
    import heapq
    if n == 0:
        return 0
    if n == 1:
        return freq[0]
    heap = [[f, 0, ""] for f in freq]
    heapq.heapify(heap)
    total = 0
    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        merged = [a[0] + b[0], 0, ""]
        total += merged[0]
        heapq.heappush(heap, merged)
    return total
