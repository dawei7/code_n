from heapq import heappop, heappush


def solve(
    n: int,
    edges: list[list[int]],
    source: int,
    destination: int,
    target: int,
) -> list[list[int]]:
    edges = [edge[:] for edge in edges]
    graph: list[list[tuple[int, int]]] = [[] for _ in range(n)]
    for index, (u, v, _) in enumerate(edges):
        graph[u].append((v, index))
        graph[v].append((u, index))

    def minimum_distances(start: int) -> list[int]:
        distances = [float("inf")] * n
        distances[start] = 0
        heap = [(0, start)]

        while heap:
            distance, node = heappop(heap)
            if distance != distances[node]:
                continue

            for neighbor, index in graph[node]:
                weight = edges[index][2]
                if weight == -1:
                    weight = 1
                candidate = distance + weight
                if candidate < distances[neighbor]:
                    distances[neighbor] = candidate
                    heappush(heap, (candidate, neighbor))

        return distances

    distance_to_destination = minimum_distances(destination)
    if distance_to_destination[source] > target:
        return []

    distances = [float("inf")] * n
    distances[source] = 0
    heap = [(0, source)]

    while heap:
        distance, node = heappop(heap)
        if distance != distances[node]:
            continue

        for neighbor, index in graph[node]:
            weight = edges[index][2]
            if weight == -1:
                weight = max(
                    1,
                    target - distance - distance_to_destination[neighbor],
                )
                edges[index][2] = weight

            candidate = distance + weight
            if candidate < distances[neighbor]:
                distances[neighbor] = candidate
                heappush(heap, (candidate, neighbor))

    if distances[destination] != target:
        return []

    for edge in edges:
        if edge[2] == -1:
            edge[2] = 2_000_000_000

    return edges


class Solution:
    def modifiedGraphEdges(
        self,
        n: int,
        edges: list[list[int]],
        source: int,
        destination: int,
        target: int,
    ) -> list[list[int]]:
        return solve(n, edges, source, destination, target)
