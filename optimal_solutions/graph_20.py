"""Optimal solution for graph_20: Travelling Salesman (Held-Karp DP).

dp[mask][i] = min cost to start at 0, visit exactly the
cities in ``mask``, and end at city i. Recurrence:
dp[mask][i] = min over j in mask of dp[mask ^ (1<<i)][j] + dist[j][i].
Final answer: min over i of dp[all][i] + dist[i][0].
"""


def solve(dist, n):
    if n <= 1:
        return 0
    INF = float("inf")
    dp = [[INF] * n for _ in range(1 << n)]
    dp[1][0] = 0
    for mask in range(1, 1 << n):
        if not (mask & 1):
            continue
        for i in range(n):
            if not (mask & (1 << i)) or dp[mask][i] == INF:
                continue
            for j in range(n):
                if mask & (1 << j):
                    continue
                new_mask = mask | (1 << j)
                new_cost = dp[mask][i] + dist[i][j]
                if new_cost < dp[new_mask][j]:
                    dp[new_mask][j] = new_cost
    full = (1 << n) - 1
    best = INF
    for i in range(n):
        if dp[full][i] < INF:
            cycle = dp[full][i] + dist[i][0]
            if cycle < best:
                best = cycle
    return best
