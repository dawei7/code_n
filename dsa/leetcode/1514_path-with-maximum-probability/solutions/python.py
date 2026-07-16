"""Optimal app-local solution for LeetCode 1514."""

import heapq


def solve(n, edges, succ_prob, start, end):
    """Return the greatest edge-probability product from start to end."""
    graph = [[] for _ in range(n)]
    for (first, second), probability in zip(edges, succ_prob):
        graph[first].append((second, probability))
        graph[second].append((first, probability))

    best = [0.0] * n
    best[start] = 1.0
    heap = [(-1.0, start)]
    while heap:
        negative_probability, node = heapq.heappop(heap)
        probability = -negative_probability
        if node == end:
            return probability
        if probability < best[node]:
            continue
        for neighbor, edge_probability in graph[node]:
            candidate = probability * edge_probability
            if candidate > best[neighbor]:
                best[neighbor] = candidate
                heapq.heappush(heap, (-candidate, neighbor))
    return 0.0
