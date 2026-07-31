from collections import deque


def solve(n: int, edges: list[list[int]]) -> list[list[int]]:
    graph = [[] for _ in range(n)]
    for first, second in edges:
        graph[first].append(second)
        graph[second].append(first)

    minimum_degree = min(map(len, graph))
    corners = {node for node in range(n) if len(graph[node]) == minimum_degree}
    start = next(iter(corners))

    parent = [-1] * n
    parent[start] = start
    queue = deque([start])
    end = start

    while queue:
        node = queue.popleft()
        if node != start and node in corners:
            end = node
            break
        for neighbor in graph[node]:
            if parent[neighbor] == -1:
                parent[neighbor] = node
                queue.append(neighbor)

    first_row = []
    while end != start:
        first_row.append(end)
        end = parent[end]
    first_row.append(start)
    first_row.reverse()

    layout = [first_row]
    used = set(first_row)

    while len(used) < n:
        next_row = []
        for node in layout[-1]:
            for neighbor in graph[node]:
                if neighbor not in used:
                    used.add(neighbor)
                    next_row.append(neighbor)
                    break
        layout.append(next_row)

    return layout
