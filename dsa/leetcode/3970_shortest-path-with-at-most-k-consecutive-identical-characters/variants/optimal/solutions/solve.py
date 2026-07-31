from heapq import heappop, heappush


def solve(n: int, edges: list[list[int]], labels: str, k: int) -> int:
    graph: list[list[tuple[int, int]]] = [[] for _ in range(n)]
    for source, destination, weight in edges:
        graph[source].append((destination, weight))

    infinity = float("inf")
    distance = [[infinity] * (k + 1) for _ in range(n)]
    distance[0][1] = 0
    heap = [(0, 0, 1)]

    while heap:
        cost, node, run_length = heappop(heap)
        if cost != distance[node][run_length]:
            continue
        if node == n - 1:
            return cost

        for neighbor, weight in graph[node]:
            next_run = run_length + 1 if labels[node] == labels[neighbor] else 1
            if next_run > k:
                continue

            next_cost = cost + weight
            if next_cost < distance[neighbor][next_run]:
                distance[neighbor][next_run] = next_cost
                heappush(heap, (next_cost, neighbor, next_run))

    return -1
