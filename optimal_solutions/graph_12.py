"""Optimal solution for graph_12: Bipartite Check.

BFS-based 2-coloring. A graph is bipartite iff no node is forced
to have the same color as an already-colored neighbor.
"""


def solve(num_nodes, edges):
    from collections import deque
    adj = [[] for _ in range(num_nodes)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    color = [-1] * num_nodes
    for start in range(num_nodes):
        if color[start] != -1:
            continue
        color[start] = 0
        q = deque([start])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 1 - color[u]
                    q.append(v)
                elif color[v] == color[u]:
                    return False
    return True
