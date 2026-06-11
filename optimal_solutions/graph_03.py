"""Optimal solution for graph_03: Depth-First Search.

Pure-graph DFS (recursive), returns visit order.
"""


def solve(num_nodes, edges):
    adj = [[] for _ in range(num_nodes)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    seen = [False] * num_nodes
    order = []

    def walk(u):
        seen[u] = True
        order.append(u)
        for v in sorted(adj[u]):
            if not seen[v]:
                walk(v)

    walk(0)
    return order
