from collections import deque


def solve(coins: list[int], edges: list[list[int]]) -> int:
    n = len(coins)
    graph = [[] for _ in range(n)]
    degree = [0] * n
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        degree[u] += 1
        degree[v] += 1

    remaining_edges = len(edges)
    queue = deque(i for i in range(n) if degree[i] == 1 and coins[i] == 0)
    while queue:
        node = queue.popleft()
        if degree[node] == 0:
            continue
        degree[node] = 0
        for nei in graph[node]:
            if degree[nei] == 0:
                continue
            remaining_edges -= 1
            degree[nei] -= 1
            if degree[nei] == 1 and coins[nei] == 0:
                queue.append(nei)

    queue = deque(i for i in range(n) if degree[i] == 1)
    for _ in range(2):
        for _ in range(len(queue)):
            node = queue.popleft()
            if degree[node] == 0:
                continue
            degree[node] = 0
            for nei in graph[node]:
                if degree[nei] == 0:
                    continue
                remaining_edges -= 1
                degree[nei] -= 1
                if degree[nei] == 1:
                    queue.append(nei)

    return max(0, remaining_edges * 2)
