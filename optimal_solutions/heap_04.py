"""Optimal solution for heap_04: Median in a Stream.

Two heaps: a max-heap of the smaller half, a min-heap of the
larger half. After each insert, rebalance so the two heaps are
within 1 of each other; the median is the top of the larger
heap (odd length) or the average of the two tops (even).
"""


def solve(data, n):
    import heapq
    if n == 0:
        return []
    small = []  # max-heap (inverted)
    large = []  # min-heap
    out = []
    for value in data:
        # Insert into the appropriate heap.
        if not small or value <= -small[0]:
            heapq.heappush(small, -value)
        else:
            heapq.heappush(large, value)
        # Rebalance.
        if len(small) > len(large) + 1:
            heapq.heappush(large, -heapq.heappop(small))
        elif len(large) > len(small):
            heapq.heappush(small, -heapq.heappop(large))
        # Compute the median.
        if len(small) > len(large):
            out.append(-small[0])
        else:
            out.append((-small[0] + large[0]) / 2)
    return out
