def solve(n: int, edges: list[list[int]], start: str, target: str) -> list[int]:
    graph: list[list[tuple[int, int]]] = [[] for _ in range(n)]
    for edge_index, (u, v) in enumerate(edges):
        graph[u].append((v, edge_index))
        graph[v].append((u, edge_index))

    parent = [-2] * n
    parent_edge = [-1] * n
    parent[0] = -1
    order = [0]

    for node in order:
        for neighbor, edge_index in graph[node]:
            if neighbor == parent[node]:
                continue
            parent[neighbor] = node
            parent_edge[neighbor] = edge_index
            order.append(neighbor)

    needs_toggle = [current != desired for current, desired in zip(start, target)]
    chosen = [False] * (n - 1)

    for node in reversed(order[1:]):
        if needs_toggle[node]:
            edge_index = parent_edge[node]
            chosen[edge_index] = True
            needs_toggle[parent[node]] = not needs_toggle[parent[node]]

    if needs_toggle[0]:
        return [-1]

    return [edge_index for edge_index, use in enumerate(chosen) if use]
