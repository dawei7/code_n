from heapq import heappop, heappush


def solve(n: int, edges: list[list[int]]) -> int:
    graph = [[] for _ in range(n)]
    for u, v, weight in edges:
        graph[u].append((v, weight))
        graph[v].append((u, weight))

    def shortest_distances(source: int) -> list[int]:
        infinity = 10**30
        distance = [infinity] * n
        distance[source] = 0
        queue = [(0, source)]
        while queue:
            current, node = heappop(queue)
            if current != distance[node]:
                continue
            for neighbor, weight in graph[node]:
                candidate = current + weight
                if candidate < distance[neighbor]:
                    distance[neighbor] = candidate
                    heappush(queue, (candidate, neighbor))
        return distance

    from_start = shortest_distances(0)
    from_target = shortest_distances(n - 1)

    answer = 10**30
    for u, v, _weight in edges:
        answer = min(
            answer,
            from_start[u] + from_target[v],
            from_start[v] + from_target[u],
        )
    return answer
