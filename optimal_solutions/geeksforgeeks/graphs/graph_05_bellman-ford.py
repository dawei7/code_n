"""Optimal solution for graph_05: Bellman-Ford.

Shortest paths from start. Supports negative edges, no negative
cycles (per the spec).
"""


def solve(num_nodes, edges, start):
    INF = float("inf")
    dist = [INF] * num_nodes
    dist[start] = 0
    for _ in range(num_nodes - 1):
        updated = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                updated = True
        if not updated:
            break
    return {i: (d if d != INF else -1) for i, d in enumerate(dist)}
