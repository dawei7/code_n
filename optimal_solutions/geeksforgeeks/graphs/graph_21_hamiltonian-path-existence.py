"""Optimal solution for graph_21: Hamiltonian Path Existence.

DFS from 0. Stop at n-1 when count == n.
"""


def solve(n, edges):
    if n <= 1:
        return n == 1
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    visited = [False] * n
    visited[0] = True

    def dfs(u, count):
        if count == n:
            return u == n - 1
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                if dfs(v, count + 1):
                    return True
                visited[v] = False
        return False

    return dfs(0, 1)
