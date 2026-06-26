"""Optimal solution for graph_04: Dijkstra.

Find shortest paths from `start` to all other nodes using a
min-heap. All edge weights are positive. O((V + E) log V) with
heapq; the simple O(V^2) version also fits the challenge budget
since the V^2 limit is generous enough.
"""


def solve(num_nodes, edges, start):
    import heapq

    # Build adjacency list (one direction; the input is "directed"
    # for the challenge's purposes, even though edges look symmetric).
    adj = {i: [] for i in range(num_nodes)}
    for u, v, w in edges:
        adj[u].append((v, w))

    dist = {i: float("inf") for i in range(num_nodes)}
    dist[start] = 0
    pq = [(0, start)]
    visited = set()
    while pq:
        d, u = heapq.heappop(pq)
        if u in visited:
            continue
        visited.add(u)
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))

    return {node: (d if d != float("inf") else -1) for node, d in dist.items()}
