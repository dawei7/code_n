"""Optimal solution for randomized_05: Karger's Min-Cut (Monte Carlo).

Given an undirected unweighted graph (with
"""


def solve(edges, n, trials):
    """Karger's min-cut algorithm with multiple trials.

    Each trial: randomly contract edges until 2 vertices
    remain. The number of remaining edges is the cut size
    for that trial. Return the minimum cut across all
    trials.
    """
    import random
    if n <= 1:
        return 0
    if n == 2:
        return len(edges)
    best = float("inf")
    for _ in range(max(1, trials)):
        # Union-Find: each vertex has a parent representative.
        parent = list(range(n))
        rank = [0] * n
        def find(x):
            r = x
            while parent[r] != r:
                r = parent[r]
            # Path compression.
            while parent[x] != r:
                parent[x], x = r, parent[x]
            return r
        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if rank[ra] < rank[rb]:
                parent[ra] = rb
            elif rank[ra] > rank[rb]:
                parent[rb] = ra
            else:
                parent[rb] = ra
                rank[ra] += 1
        # Run one trial: shuffle edges and contract until
        # 2 components remain. The contracted multigraph
        # has parallel edges; we model it by keeping all
        # edges and counting "alive" ones.
        live_edges = list(edges)
        random.shuffle(live_edges)
        # Number of components = number of distinct roots.
        num_components = n
        for u, v in live_edges:
            if num_components <= 2:
                break
            ru, rv = find(u), find(v)
            if ru == rv:
                # Self-loop in the contracted graph; ignore.
                continue
            union(ru, rv)
            num_components -= 1
        # Count cut edges: edges (u, v) with find(u) != find(v).
        cut = 0
        for u, v in edges:
            if find(u) != find(v):
                cut += 1
        if cut < best:
            best = cut
    return best
