"""Optimal solution for approx_07: 0/1 Knapsack FPTAS.

Given n items with values and weights and capacity
"""


def solve(values, weights, n, capacity, eps):
    """0/1 Knapsack FPTAS: scale values, run DP, return result."""
    if capacity <= 0 or n == 0:
        return 0
    v_max = max(values) if values else 1
    if v_max == 0:
        return 0
    K = (eps * v_max) / n
    if K <= 0:
        K = 1
    scaled = [max(1, int(v / K)) for v in values]
    # DP: dp[w] = max scaled value for weight w.
    dp = [0] * (capacity + 1)
    for i in range(n):
        wi = min(weights[i], capacity)
        vi = scaled[i]
        for w in range(capacity, wi - 1, -1):
            cand = dp[w - wi] + vi
            if cand > dp[w]:
                dp[w] = cand
    return dp[capacity] * K
