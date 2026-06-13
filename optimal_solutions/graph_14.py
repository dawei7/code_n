"""Optimal solution for graph_14: Bridges.

Tarjan-style DFS on an undirected graph. An edge (u, v) is a
bridge iff, in the DFS tree, ``low[v] > disc[u]``. The result
is the sorted list of (u, v) bridge tuples with u < v.
"""


def solve(num_nodes, edges):
    if num_nodes <= 0:
        return []
    adj = [set() for _ in range(num_nodes)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    disc = [-1] * num_nodes
    low = [0] * num_nodes
    bridges = set()

    def dfs(u, parent, time):
        disc[u] = low[u] = time
        time += 1
        for v in sorted(adj[u]):
            if disc[v] == -1:
                time = dfs(v, u, time)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:
                    bridges.add((min(u, v), max(u, v)))
            elif v != parent:
                low[u] = min(low[u], disc[v])
        return time

    dfs(0, -1, 0)
    return sorted(bridges)
