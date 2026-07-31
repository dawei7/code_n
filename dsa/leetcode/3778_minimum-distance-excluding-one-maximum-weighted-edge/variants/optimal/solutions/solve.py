from heapq import heappop, heappush
from typing import List


def solve(n: int, edges: List[List[int]]) -> int:
    graph = [[] for _ in range(n)]
    for u, v, weight in edges:
        graph[u].append((v, weight))
        graph[v].append((u, weight))
    infinity = 10**30
    distance = [[infinity, infinity] for _ in range(n)]
    distance[0][0] = 0
    queue = [(0, 0, 0)]
    while queue:
        cost, node, excluded = heappop(queue)
        if cost != distance[node][excluded]:
            continue
        if node == n - 1 and excluded:
            return cost
        for neighbor, weight in graph[node]:
            paid_cost = cost + weight
            if paid_cost < distance[neighbor][excluded]:
                distance[neighbor][excluded] = paid_cost
                heappush(queue, (paid_cost, neighbor, excluded))
            if not excluded and cost < distance[neighbor][1]:
                distance[neighbor][1] = cost
                heappush(queue, (cost, neighbor, 1))
    return distance[n - 1][1]
