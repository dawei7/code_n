from heapq import heappop, heappush


def solve(n: int, edges: list[list[int]], threshold: int) -> int:
    reverse_graph: list[list[tuple[int, int]]] = [[] for _ in range(n)]
    for source, destination, weight in edges:
        reverse_graph[destination].append((source, weight))

    best = [float("inf")] * n
    best[0] = 0
    heap: list[tuple[int, int]] = [(0, 0)]

    while heap:
        cost, node = heappop(heap)
        if cost != best[node]:
            continue

        for predecessor, weight in reverse_graph[node]:
            candidate = max(cost, weight)
            if candidate < best[predecessor]:
                best[predecessor] = candidate
                heappush(heap, (candidate, predecessor))

    answer = max(best)
    return -1 if answer == float("inf") else int(answer)
