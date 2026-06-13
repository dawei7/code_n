"""Optimal solution for approx_03: TSP via MST (2-Approx).

Given a complete graph with edge costs that satisfy
"""


def solve(cost, n):
    """MST-based 2-approximate TSP.

    1. Build MST rooted at 0 via Prim's.
    2. Preorder walk of the MST to produce a tour.
    3. Sum the costs along the tour (including the return
       edge from the last vertex back to 0).
    """
    if n <= 1:
        return 0
    INF = float("inf")
    # Prim's MST.
    in_mst = [False] * n
    in_mst[0] = True
    # parent[i] = the node that brought i into the MST.
    parent = [-1] * n
    for _ in range(n - 1):
        best_w = INF
        best_v = -1
        for u in range(n):
            if not in_mst[u]:
                continue
            for v in range(n):
                if in_mst[v]:
                    continue
                if cost[u][v] < best_w:
                    best_w = cost[u][v]
                    best_v = v
                    parent[v] = u
        if best_v == -1:
            break
        in_mst[best_v] = True
    # Preorder DFS walk of the MST.
    children = [[] for _ in range(n)]
    for v in range(n):
        p = parent[v]
        if p != -1:
            children[p].append(v)
    tour = []
    def dfs(u):
        tour.append(u)
        for c in children[u]:
            dfs(c)
    dfs(0)
    # Sum tour cost (including the return edge).
    total = 0
    for i in range(len(tour) - 1):
        total += cost[tour[i]][tour[i + 1]]
    total += cost[tour[-1]][0]
    return total
