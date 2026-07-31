from heapq import heappop, heappush


def solve(n: int, edges: list[list[int]]) -> list[bool]:
    graph = [[] for _ in range(n)]
    for start, end, weight in edges:
        graph[start].append((end, weight))
        graph[end].append((start, weight))

    def distances(source: int) -> list[int]:
        result = [float("inf")] * n
        result[source] = 0
        heap = [(0, source)]

        while heap:
            distance, node = heappop(heap)
            if distance != result[node]:
                continue
            for neighbor, weight in graph[node]:
                candidate = distance + weight
                if candidate < result[neighbor]:
                    result[neighbor] = candidate
                    heappush(heap, (candidate, neighbor))

        return result

    from_start = distances(0)
    from_end = distances(n - 1)
    shortest = from_start[n - 1]

    return [
        shortest < float("inf")
        and (
            from_start[start] + weight + from_end[end] == shortest
            or from_start[end] + weight + from_end[start] == shortest
        )
        for start, end, weight in edges
    ]
