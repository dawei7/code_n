import heapq


def solve(n: int, edges: list[list[int]]) -> int:
    graph: list[list[tuple[int, int]]] = [[] for _ in range(n)]
    for source, target, weight in edges:
        graph[source].append((target, weight))
        graph[target].append((source, 2 * weight))

    distances = [float("inf")] * n
    distances[0] = 0
    queue = [(0, 0)]

    while queue:
        distance, node = heapq.heappop(queue)
        if distance != distances[node]:
            continue
        if node == n - 1:
            return distance

        for neighbor, cost in graph[node]:
            candidate = distance + cost
            if candidate < distances[neighbor]:
                distances[neighbor] = candidate
                heapq.heappush(queue, (candidate, neighbor))

    return -1
