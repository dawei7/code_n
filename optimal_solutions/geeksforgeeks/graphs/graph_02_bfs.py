"""Optimal solution for graph_02: Breadth-First Search.

Pure-graph BFS on adjacency lists, returns visit order.
"""


def solve(num_nodes, edges):
    from collections import deque
    adj = [[] for _ in range(num_nodes)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    seen = [False] * num_nodes
    order = []
    q = deque([0])
    seen[0] = True
    while q:
        u = q.popleft()
        order.append(u)
        for v in sorted(adj[u]):
            if not seen[v]:
                seen[v] = True
                q.append(v)
    return order
