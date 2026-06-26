"""Optimal solution for flow_03: Bipartite Matching.

Reduce to max flow: source -> left (cap 1) -> right (cap 1) -> sink.
Max flow = max matching size.
"""


def solve(left_n, right_n, edges):
    from collections import deque
    n = left_n + right_n + 2
    source = 0
    sink = n - 1
    cap = [[0] * n for _ in range(n)]
    for u, v in edges:
        cap[1 + u][1 + left_n + v] += 1
    for u in range(left_n):
        cap[source][1 + u] += 1
    for v in range(right_n):
        cap[1 + left_n + v][sink] += 1
    flow = 0
    while True:
        parent = [-1] * n
        parent[source] = source
        q = deque([source])
        visited = [False] * n
        visited[source] = True
        while q and parent[sink] == -1:
            u = q.popleft()
            for v in range(n):
                if not visited[v] and cap[u][v] > 0:
                    visited[v] = True
                    parent[v] = u
                    q.append(v)
        if parent[sink] == -1:
            break
        path_flow = float("inf")
        v = sink
        while v != source:
            u = parent[v]
            if cap[u][v] < path_flow:
                path_flow = cap[u][v]
            v = u
        v = sink
        while v != source:
            u = parent[v]
            cap[u][v] -= path_flow
            cap[v][u] += path_flow
            v = u
        flow += path_flow
    return flow
