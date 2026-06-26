"""Optimal solution for heap_05: Sliding Window Maximum.

For each window of size k, return the max. Use a max-heap keyed
on (-value, index); pop from the top while the index is outside
the current window.
"""


def solve(arr, k, n):
    if k <= 0 or k > n:
        return []
    import heapq
    heap = []
    for i in range(k):
        heapq.heappush(heap, (-arr[i], i))
    out = [-heap[0][0]]
    for i in range(k, n):
        heapq.heappush(heap, (-arr[i], i))
        while heap[0][1] <= i - k:
            heapq.heappop(heap)
        out.append(-heap[0][0])
    return out
