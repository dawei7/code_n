"""Optimal solution for graph_17: 0-1 BFS.

Shortest path on a graph with edge weights in {0, 1}. Use a
deque: pop the left, push 0-weight neighbors to the LEFT and
1-weight neighbors to the RIGHT. This is O(V + E).
"""


def solve(num_nodes, edges, start):
    if num_nodes <= 0:
        return {}
    adj = [[] for _ in range(num_nodes)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    INF = float("inf")
    dist = [INF] * num_nodes
    dist[start] = 0
    from collections import deque
    dq = deque([start])
    while dq:
        u = dq.popleft()
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                if w == 0:
                    dq.appendleft(v)
                else:
                    dq.append(v)
    return {i: (-1 if dist[i] == INF else dist[i]) for i in range(num_nodes)}
