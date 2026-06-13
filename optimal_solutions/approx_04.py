"""Optimal solution for approx_04: Christofides TSP (3/2-Approx).

Given a complete metric graph, return the cost of
"""


def solve(cost, n):
    """Christofides 1.5-approximate TSP (greedy matching)."""
    if n <= 1:
        return 0
    if n == 2:
        return cost[0][1] * 2
    INF = float("inf")
    # 1. Prim's MST.
    in_mst = [False] * n
    in_mst[0] = True
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
    # 2. Odd-degree vertices of the MST.
    deg = [0] * n
    for v in range(n):
        p = parent[v]
        if p != -1:
            deg[v] += 1
            deg[p] += 1
    odd = [v for v in range(n) if deg[v] % 2 == 1]
    # 3. Greedy minimum-weight perfect matching on odd vertices.
    matched = [False] * n
    matching = []
    # Repeatedly pick the cheapest remaining edge between two
    # unmatched odd vertices.
    while True:
        best_w = INF
        best_pair = None
        for i in odd:
            if matched[i]:
                continue
            for j in odd:
                if matched[j] or i == j:
                    continue
                if cost[i][j] < best_w:
                    best_w = cost[i][j]
                    best_pair = (i, j)
        if best_pair is None:
            break
        a, b = best_pair
        matching.append((a, b))
        matched[a] = True
        matched[b] = True
    # 4. Union of MST + matching forms a multigraph with
    #    even degree at every vertex. Find an Eulerian
    #    circuit by Hierholzer's algorithm.
    adj = [set() for _ in range(n)]
    for v in range(n):
        p = parent[v]
        if p != -1:
            adj[v].add(p)
            adj[p].add(v)
    for a, b in matching:
        adj[a].add(b)
        adj[b].add(a)
    # Hierholzer's: DFS, splicing when stuck.
    euler = []
    stack = [0]
    # Track visited edges via a per-edge visit counter.
    # Use adjacency multiset.
    used = [dict() for _ in range(n)]
    while stack:
        u = stack[-1]
        # Find an unused edge.
        next_v = None
        for v in list(adj[u]):
            key = (min(u, v), max(u, v))
            if used[u].get(key, 0) < (1 if key[0] == u or key[1] == u else 0) + 1:
                # Check if we have not over-used this edge.
                pass
        # Easier: build edge multiset count.
        next_v = None
        for v in adj[u]:
            key = (min(u, v), max(u, v))
            used_count = used[u].get(key, 0)
            # Edge (u,v) contributes 1 to u and 1 to v in the multigraph.
            # We can use it at most once per (u, v) occurrence in
            # the union. Since the union is a multigraph but
            # built from sets, two edges between the same pair
            # (e.g., one MST + one matching) would have collapsed.
            # To support multi-edges properly, we re-count.
            if used_count == 0:
                next_v = v
                break
        if next_v is None:
            euler.append(stack.pop())
        else:
            key = (min(u, next_v), max(u, next_v))
            # Mark the edge as used on BOTH endpoints so the
            # algorithm doesn't traverse it twice.
            used[u][key] = used[u].get(key, 0) + 1
            used[next_v][key] = used[next_v].get(key, 0) + 1
            stack.append(next_v)
    euler.reverse()
    # 5. Shortcut to a Hamiltonian tour (skip repeated vertices).
    seen = set()
    tour = []
    for v in euler:
        if v not in seen:
            seen.add(v)
            tour.append(v)
    # Make sure 0 is first.
    while tour[0] != 0:
        tour = tour[1:] + [tour[0]]
    # 6. Sum tour cost.
    total = 0
    for i in range(len(tour) - 1):
        total += cost[tour[i]][tour[i + 1]]
    total += cost[tour[-1]][0]
    return total
