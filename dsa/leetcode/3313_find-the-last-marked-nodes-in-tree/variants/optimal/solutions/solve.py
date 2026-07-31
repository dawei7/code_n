from collections import deque


def solve(edges: list[list[int]]) -> list[int]:
    n = len(edges) + 1
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    def distances(start: int) -> tuple[int, list[int]]:
        dist = [-1] * n
        dist[start] = 0
        queue = deque([start])
        farthest = start

        while queue:
            node = queue.popleft()
            if dist[node] > dist[farthest]:
                farthest = node
            for neighbor in graph[node]:
                if dist[neighbor] == -1:
                    dist[neighbor] = dist[node] + 1
                    queue.append(neighbor)

        return farthest, dist

    endpoint_a, _ = distances(0)
    endpoint_b, dist_a = distances(endpoint_a)
    _, dist_b = distances(endpoint_b)

    return [endpoint_a if dist_a[node] > dist_b[node] else endpoint_b for node in range(n)]
