"""Optimal solution for approx_01: Vertex Cover (2-Approx).

Greedy: pick the max-degree vertex, drop its edges, repeat.
"""


def solve(n, edges):
    if n == 0:
        return set()
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    cover = set()
    edges_left = set()
    for u, v in edges:
        edges_left.add((min(u, v), max(u, v)))
    while edges_left:
        degrees = [0] * n
        for u, v in edges_left:
            degrees[u] += 1
            degrees[v] += 1
        v = max(range(n), key=lambda i: degrees[i])
        if degrees[v] == 0:
            break
        cover.add(v)
        edges_to_remove = [e for e in edges_left if v in e]
        for e in edges_to_remove:
            edges_left.discard(e)
    return sorted(cover)
