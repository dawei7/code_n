"""Optimal solution for flow_05: Minimum s-t Cut.

Find the minimum s-t cut in a directed flow network.
"""


def solve(n, edges):
    """Min s-t cut via max-flow then residual reachability.

    Returns a sorted list of (u, v) tuples for the cut.
    """
    from collections import deque
    INF = float("inf")
    # Build a fresh capacity matrix.
    cap = [[0] * n for _ in range(n)]
    for u, v, c in edges:
        cap[u][v] += c
    # Ford-Fulkerson with BFS (Edmonds-Karp) on the residual.
    flow = 0
    while True:
        parent = [-1] * n
        parent[0] = 0
        q = deque([0])
        visited = [False] * n
        visited[0] = True
        while q and parent[n - 1] == -1:
            u = q.popleft()
            for v in range(n):
                if not visited[v] and cap[u][v] > 0:
                    visited[v] = True
                    parent[v] = u
                    q.append(v)
        if parent[n - 1] == -1:
            break
        path_flow = INF
        v = n - 1
        while v != 0:
            u = parent[v]
            if cap[u][v] < path_flow:
                path_flow = cap[u][v]
            v = u
        v = n - 1
        while v != 0:
            u = parent[v]
            cap[u][v] -= path_flow
            cap[v][u] += path_flow
            v = u
        flow += path_flow
    # Now DFS from s in the residual to find reachable set.
    reachable = [False] * n
    reachable[0] = True
    stack = [0]
    while stack:
        u = stack.pop()
        for v in range(n):
            if not reachable[v] and cap[u][v] > 0:
                reachable[v] = True
                stack.append(v)
    # Cut edges: original edges from reachable to non-reachable.
    cut = []
    for u, v, c in edges:
        if reachable[u] and not reachable[v]:
            cut.append((u, v))
    cut.sort()
    return cut
