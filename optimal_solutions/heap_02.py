"""Optimal solution for heap_02: Kth Largest Element.

Maintain a min-heap of size k. For each element, push it onto
the heap and pop the smallest if the heap is over k. At the end
the heap contains the k largest elements; the smallest of those
(the heap top) is the kth largest. O(n log k).
"""


def solve(data, n, k):
    import heapq
    if k <= 0 or k > n:
        return -1
    heap = []
    for value in data:
        if len(heap) < k:
            heapq.heappush(heap, value)
        elif value > heap[0]:
            heapq.heapreplace(heap, value)
    return heap[0]
