from collections import deque


def solve(graph: list[list[int]]) -> list[int]:
    reverse_graph = [[] for _ in graph]
    remaining = [len(neighbors) for neighbors in graph]
    for node, neighbors in enumerate(graph):
        for neighbor in neighbors:
            reverse_graph[neighbor].append(node)

    queue = deque(node for node, degree in enumerate(remaining) if degree == 0)
    safe = [False] * len(graph)
    while queue:
        node = queue.popleft()
        safe[node] = True
        for predecessor in reverse_graph[node]:
            remaining[predecessor] -= 1
            if remaining[predecessor] == 0:
                queue.append(predecessor)

    return [node for node, is_safe in enumerate(safe) if is_safe]
