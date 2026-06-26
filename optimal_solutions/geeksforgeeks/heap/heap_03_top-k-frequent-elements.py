"""Optimal solution for heap_03: Top K Frequent Elements.

Count occurrences with a hash map, then push (count, value) into
a max-heap. Pop the top k. The output is sorted in DESCENDING
order of frequency; ties broken by value in DESCENDING order so
the verify can do a plain equality check.
"""


def solve(data, n, k):
    import heapq
    if k <= 0 or n == 0:
        return []
    counts = {}
    for value in data:
        counts[value] = counts.get(value, 0) + 1
    # Max-heap via (-count, -value). Inverting both ensures ties
    # are broken by DESCENDING value (the smaller -v comes first).
    heap = [(-c, -v) for v, c in counts.items()]
    heapq.heapify(heap)
    out = []
    for _ in range(min(k, len(heap))):
        neg_c, neg_v = heapq.heappop(heap)
        out.append(-neg_v)
    return out
