"""Optimal solution for heap_06: Kth Smallest in a Sorted Matrix.

A matrix where every row and every column is sorted. The first
column is not necessarily sorted, but the matrix has the property
that the smallest element is in [0][0]. Use a min-heap of
(value, row, col) and pop k times.
"""


def solve(matrix, n, k):
    if n == 0 or k <= 0:
        return -1
    import heapq
    heap = [(matrix[0][0], 0, 0)]
    seen = {(0, 0)}
    popped = 0
    while heap:
        v, r, c = heapq.heappop(heap)
        popped += 1
        if popped == k:
            return v
        for dr, dc in [(0, 1), (1, 0)]:
            nr, nc = r + dr, c + dc
            if nr < n and nc < n and (nr, nc) not in seen:
                heapq.heappush(heap, (matrix[nr][nc], nr, nc))
                seen.add((nr, nc))
    return -1
