"""Optimal solution for graph_13: Articulation Points.

Tarjan-style DFS on an undirected graph. A node u is an
articulation point iff one of its DFS-tree children v has
``low[v] >= disc[u]`` (and u is not the root, OR u is the
root with more than one DFS child). The result is the sorted
list of articulation point indices.
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
    parent = [-1] * num_nodes
    ap = set()

    def dfs(u, time):
        disc[u] = low[u] = time
        time += 1
        children = 0
        for v in sorted(adj[u]):
            if disc[v] == -1:
                parent[v] = u
                children += 1
                time = dfs(v, time)
                low[u] = min(low[u], low[v])
                if parent[u] == -1 and children > 1:
                    ap.add(u)
                if parent[u] != -1 and low[v] >= disc[u]:
                    ap.add(u)
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])
        return time

    dfs(0, 0)
    return sorted(ap)
