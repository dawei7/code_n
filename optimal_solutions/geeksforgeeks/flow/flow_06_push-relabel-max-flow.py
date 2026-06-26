"""Optimal solution for flow_06: Push-Relabel Max Flow.

Compute the max s-t flow using the Goldberg-Tarjan
"""


def solve(n, edges):
    """Goldberg-Tarjan push-relabel max flow.

    Generic O(V^3) variant. The residual capacity of an edge
    (u, v) is maintained as a direct value (not cap-flow),
    so a push that decreases residual[u][v] increases
    residual[v][u] by the same amount.
    """
    # residual[u][v] = remaining forward capacity from u to v.
    residual = [[0] * n for _ in range(n)]
    for u, v, c in edges:
        residual[u][v] += c
    height = [0] * n
    excess = [0] * n
    height[0] = n
    # Initial push from source: saturate every outgoing edge.
    for v in range(n):
        if residual[0][v] > 0:
            pushed = residual[0][v]
            residual[0][v] -= pushed
            residual[v][0] += pushed
            excess[v] += pushed

    def push(u, v):
        d = min(excess[u], residual[u][v])
        if d <= 0:
            return False
        residual[u][v] -= d
        residual[v][u] += d
        excess[u] -= d
        excess[v] += d
        return True

    def relabel(u):
        best = float("inf")
        for v in range(n):
            if residual[u][v] > 0 and height[v] < best:
                best = height[v]
        if best < float("inf"):
            height[u] = best + 1

    # Main loop: discharge active vertices (those with positive
    # excess that are not s or t). When a push creates new
    # excess at an inner vertex, add it to the active list.
    active = set()
    for i in range(1, n - 1):
        if excess[i] > 0:
            active.add(i)
    while active:
        # Highest-label selection.
        u = max(active, key=lambda x: height[x])
        old_h = height[u]
        # Discharge: try to push, or relabel.
        while excess[u] > 0:
            pushed = False
            for v in range(n):
                if residual[u][v] > 0 and height[u] == height[v] + 1:
                    if push(u, v):
                        pushed = True
                        if v != 0 and v != n - 1 and excess[v] > 0:
                            active.add(v)
                        break
            if not pushed:
                relabel(u)
        if excess[u] == 0:
            active.discard(u)
    return excess[n - 1]
