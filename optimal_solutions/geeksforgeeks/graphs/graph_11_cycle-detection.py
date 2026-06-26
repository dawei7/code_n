"""Optimal solution for graph_11: Cycle Detection (Undirected).

Iterative DFS with parent tracking. A back-edge to a non-parent
visited node is a cycle.
"""


def solve(num_nodes, edges):
    adj = [[] for _ in range(num_nodes)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    visited = [False] * num_nodes
    for start in range(num_nodes):
        if visited[start]:
            continue
        stack = [(start, -1)]
        visited[start] = True
        while stack:
            u, parent = stack.pop()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    stack.append((v, u))
                elif v != parent:
                    return True
    return False
