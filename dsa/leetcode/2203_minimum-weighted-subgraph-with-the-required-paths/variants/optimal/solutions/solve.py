from heapq import heappop, heappush


def solve(
    n: int,
    edges: list[list[int]],
    src1: int,
    src2: int,
    dest: int,
) -> int:
    graph = [[] for _ in range(n)]
    reverse = [[] for _ in range(n)]
    for source, target, weight in edges:
        graph[source].append((target, weight))
        reverse[target].append((source, weight))

    def dijkstra(start: int, adjacency: list[list[tuple[int, int]]]):
        distance = [float("inf")] * n
        distance[start] = 0
        heap = [(0, start)]

        while heap:
            current, node = heappop(heap)
            if current != distance[node]:
                continue
            for neighbor, weight in adjacency[node]:
                candidate = current + weight
                if candidate < distance[neighbor]:
                    distance[neighbor] = candidate
                    heappush(heap, (candidate, neighbor))
        return distance

    from_first = dijkstra(src1, graph)
    from_second = dijkstra(src2, graph)
    to_destination = dijkstra(dest, reverse)

    answer = min(from_first[node] + from_second[node] + to_destination[node] for node in range(n))
    return -1 if answer == float("inf") else answer
