"""Optimal app-local solution for LeetCode 3604."""

from heapq import heappop, heappush


def solve(n, edges):
    graph = [[] for _ in range(n)]
    for source, destination, start, end in edges:
        graph[source].append((destination, start, end))

    infinity = float("inf")
    earliest = [infinity] * n
    earliest[0] = 0
    queue = [(0, 0)]

    while queue:
        time, node = heappop(queue)
        if time != earliest[node]:
            continue
        if node == n - 1:
            return time

        for neighbor, start, end in graph[node]:
            if time > end:
                continue
            arrival = max(time, start) + 1
            if arrival < earliest[neighbor]:
                earliest[neighbor] = arrival
                heappush(queue, (arrival, neighbor))

    return -1
