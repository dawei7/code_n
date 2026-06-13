"""Optimal solution for flow_01: Ford-Fulkerson Max Flow.

DFS-based augmenting path. Find path, push bottleneck,
update residual. Repeat.
"""


def solve(n, edges):
    INF = float("inf")
    cap = [[0] * n for _ in range(n)]
    for u, v, c in edges:
        cap[u][v] += c
    max_flow = 0
    while True:
        parent = [-1] * n
        parent[0] = 0
        stack = [0]
        visited = [False] * n
        visited[0] = True
        found = -1
        while stack and found == -1:
            u = stack.pop()
            for v in range(n):
                if not visited[v] and cap[u][v] > 0:
                    visited[v] = True
                    parent[v] = u
                    if v == n - 1:
                        found = v
                        break
                    stack.append(v)
        if found == -1:
            break
        path_flow = float("inf")
        v = found
        while v != 0:
            u = parent[v]
            if cap[u][v] < path_flow:
                path_flow = cap[u][v]
            v = u
        v = found
        while v != 0:
            u = parent[v]
            cap[u][v] -= path_flow
            cap[v][u] += path_flow
            v = u
        max_flow += path_flow
    return max_flow
