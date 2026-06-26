"""Optimal solution for dp_28: Bellman-Ford (SSSP).

Relax all edges n-1 times.
"""


def solve(n, edges, src):
    INF = 10 ** 9
    dist = [INF] * n
    dist[src] = 0
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    return dist
