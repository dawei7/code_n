"""Optimal solution for graph_10: Prim's MST.

Vertex-growth MST using a min-heap of (weight, from, to) edges.
"""


def solve(num_nodes, edges):
    import heapq
    if num_nodes == 0:
        return []
    adj = [[] for _ in range(num_nodes)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    visited = [False] * num_nodes
    visited[0] = True
    heap = []
    for v, w in adj[0]:
        heapq.heappush(heap, (w, 0, v))
    mst = []
    while heap:
        w, u, v = heapq.heappop(heap)
        if visited[v]:
            continue
        visited[v] = True
        mst.append((u, v, w))
        for nxt, w2 in adj[v]:
            if not visited[nxt]:
                heapq.heappush(heap, (w2, v, nxt))
    if len(mst) != num_nodes - 1:
        return []
    return sorted(mst)
