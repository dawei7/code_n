"""Optimal solution for flow_04: Dinic's Max Flow.

Compute the max s-t flow in a directed capacitated
"""


def solve(n, edges):
    """Dinic's max flow on an adjacency-matrix residual graph.

    Returns the max flow from 0 to n-1.
    """
    from collections import deque
    INF = float("inf")
    cap = [[0] * n for _ in range(n)]
    for u, v, c in edges:
        cap[u][v] += c
    flow = 0
    while True:
        # BFS builds the level graph.
        level = [-1] * n
        level[0] = 0
        q = deque([0])
        while q:
            u = q.popleft()
            for v in range(n):
                if level[v] < 0 and cap[u][v] > 0:
                    level[v] = level[u] + 1
                    q.append(v)
        if level[n - 1] < 0:
            break
        # DFS sends blocking flow along level-monotone paths.
        it = [0] * n
        def dfs(u, f):
            if u == n - 1:
                return f
            for i in range(it[u], n):
                v = i
                it[u] = i
                if level[v] == level[u] + 1 and cap[u][v] > 0:
                    pushed = dfs(v, min(f, cap[u][v]))
                    if pushed:
                        cap[u][v] -= pushed
                        cap[v][u] += pushed
                        return pushed
            return 0
        while True:
            pushed = dfs(0, INF)
            if not pushed:
                break
            flow += pushed
    return flow
