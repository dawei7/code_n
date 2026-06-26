"""Optimal solution for graph_07: Topological Sort.

Kahn's BFS-based topological sort. -1 on cycle (setup guarantees
a DAG, so the answer is always a list).
"""


def solve(num_nodes, edges):
    from collections import deque
    adj = [[] for _ in range(num_nodes)]
    indeg = [0] * num_nodes
    for u, v in edges:
        adj[u].append(v)
        indeg[v] += 1
    q = deque()
    for i in range(num_nodes):
        if indeg[i] == 0:
            q.append(i)
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in sorted(adj[u]):
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    if len(order) != num_nodes:
        return -1
    return order
