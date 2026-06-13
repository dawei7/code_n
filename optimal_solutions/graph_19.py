"""Optimal solution for graph_19: M-Coloring Problem.

Return True iff the graph can be colored with m colors
such that no two adjacent vertices share a color.

Backtracking: assign colors to vertices one at a time.
At each step, try each color; if it doesn't conflict with
any already-colored neighbor, recurse.
"""


def solve(n, edges, m):
    if n == 0:
        return True
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    color = [-1] * n

    def safe(v, c):
        for u in adj[v]:
            if color[u] == c:
                return False
        return True

    def helper(v):
        if v == n:
            return True
        for c in range(m):
            if safe(v, c):
                color[v] = c
                if helper(v + 1):
                    return True
                color[v] = -1
        return False

    return helper(0)
