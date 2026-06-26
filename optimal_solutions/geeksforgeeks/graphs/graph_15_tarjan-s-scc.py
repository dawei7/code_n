"""Optimal solution for graph_15: Tarjan's SCC.

Single-pass DFS on a directed graph that maintains each node's
discovery time and low-link value. When low[u] == disc[u], u
is the root of an SCC; pop the stack until u is removed.
Returns a list of SCCs, each sorted; outer list sorted by
smallest element.
"""


def solve(num_nodes, edges):
    if num_nodes <= 0:
        return []
    adj = [[] for _ in range(num_nodes)]
    for u, v in edges:
        adj[u].append(v)
    disc = [-1] * num_nodes
    low = [0] * num_nodes
    on_stack = [False] * num_nodes
    stack = []
    sccs = []

    def dfs(u, time):
        disc[u] = low[u] = time
        time += 1
        stack.append(u)
        on_stack[u] = True
        for v in sorted(adj[u]):
            if disc[v] == -1:
                time = dfs(v, time)
                low[u] = min(low[u], low[v])
            elif on_stack[v]:
                low[u] = min(low[u], disc[v])
        if low[u] == disc[u]:
            component = []
            while True:
                w = stack.pop()
                on_stack[w] = False
                component.append(w)
                if w == u:
                    break
            sccs.append(sorted(component))
        return time

    for start in range(num_nodes):
        if disc[start] == -1:
            dfs(start, 0)
    return sorted(sccs, key=lambda c: c[0])
