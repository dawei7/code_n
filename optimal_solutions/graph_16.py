"""Optimal solution for graph_16: Kosaraju's SCC.

Two-pass DFS on a directed graph. Pass 1 walks the original
graph, pushing each node onto a stack when its DFS finishes.
Pass 2 walks the transpose graph in stack-pop order; each DFS
tree in pass 2 is one SCC. Outer list sorted by smallest
element.
"""


def solve(num_nodes, edges):
    if num_nodes <= 0:
        return []
    adj = [[] for _ in range(num_nodes)]
    radj = [[] for _ in range(num_nodes)]
    for u, v in edges:
        adj[u].append(v)
        radj[v].append(u)
    visited = [False] * num_nodes
    order = []

    def dfs1(u):
        visited[u] = True
        for v in sorted(adj[u]):
            if not visited[v]:
                dfs1(v)
        order.append(u)

    for u in range(num_nodes):
        if not visited[u]:
            dfs1(u)
    visited = [False] * num_nodes
    sccs = []

    def dfs2(u, comp):
        visited[u] = True
        comp.append(u)
        for v in sorted(radj[u]):
            if not visited[v]:
                dfs2(v, comp)

    for u in reversed(order):
        if not visited[u]:
            comp = []
            dfs2(u, comp)
            sccs.append(sorted(comp))
    return sorted(sccs, key=lambda c: c[0])
