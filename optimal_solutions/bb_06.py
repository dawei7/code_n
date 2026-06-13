"""Optimal solution for bb_06: TSP via Reduced Matrix (B&B).

Solve the traveling salesman problem using the
"""


def solve(cost, n):
    """TSP via reduced-matrix LC branch and bound.

    Each live node has: (lb, path, matrix, cost_so_far).
    Lower bound = path cost + row/column reduction cost.
    Branching: include or exclude the next edge from the
    current node to an unvisited city.
    """
    INF = float("inf")
    N_MAX = 12
    if n <= 1:
        return 0
    if n == 2:
        return cost[0][1] + cost[1][0]

    def reduce(mat):
        """Return (reduced_matrix, reduction_cost)."""
        red = [row[:] for row in mat]
        reduction = 0
        # Row reduction.
        for i in range(n):
            finite = [v for v in red[i] if v < INF]
            if not finite:
                continue
            min_val = min(finite)
            if min_val == 0:
                continue
            reduction += min_val
            for j in range(n):
                if red[i][j] < INF:
                    red[i][j] -= min_val
        # Column reduction.
        for j in range(n):
            col_vals = [red[i][j] for i in range(n) if red[i][j] < INF]
            if not col_vals:
                continue
            min_val = min(col_vals)
            if min_val == 0:
                continue
            reduction += min_val
            for i in range(n):
                if red[i][j] < INF:
                    red[i][j] -= min_val
        return red, reduction

    # Each priority queue entry:
    # (lb, path_tuple, matrix, cost_so_far, parent_reduction)
    # lb = cost_so_far + (current reduction). The reduction at
    # this node has been accounted for in `lb`; for the child,
    # we use: new_lb = lb + edge_cost + (new_reduction - old_reduction).
    import heapq
    root_red, root_red_cost = reduce(cost)
    pq = [(root_red_cost, (0,), tuple(tuple(row) for row in root_red), 0, root_red_cost)]
    best = INF
    while pq:
        lb, path, mat_t, cost_so_far, parent_red = heapq.heappop(pq)
        if lb >= best:
            continue
        if len(path) == n:
            # Complete tour: return to start.
            total = cost_so_far + cost[path[-1]][0]
            if total < best:
                best = total
            continue
        # Branch: try each unvisited city from path[-1].
        cur = path[-1]
        for nxt in range(n):
            if nxt in path:
                continue
            edge_cost = cost[cur][nxt]
            if edge_cost >= INF:
                continue
            new_mat = [list(row) for row in mat_t]
            for j in range(n):
                new_mat[cur][j] = INF
            for i in range(n):
                new_mat[i][nxt] = INF
            new_mat[nxt][0] = INF
            new_red, new_red_cost = reduce(new_mat)
            new_lb = lb + edge_cost + (new_red_cost - parent_red)
            if new_lb < best:
                new_path = path + (nxt,)
                heapq.heappush(pq, (new_lb, new_path,
                                    tuple(tuple(row) for row in new_red),
                                    cost_so_far + edge_cost,
                                    new_red_cost))
    return best if best < INF else -1
