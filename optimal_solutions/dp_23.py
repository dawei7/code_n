"""Optimal solution for dp_23: Min Cost Climbing Stairs.

Minimum cost to reach the top of a staircase where you
may climb 1 or 2 steps at a time. cost[i] is the cost of
step i. dp[i] = cost[i] + min(dp[i-1], dp[i-2]). The
answer is min(dp[n-1], dp[n-2]).
"""


def solve(cost, n):
    if n == 0:
        return 0
    if n == 1:
        return cost[0]
    prev2 = cost[0]
    prev1 = cost[1]
    for i in range(2, n):
        cur = cost[i] + min(prev1, prev2)
        prev2, prev1 = prev1, cur
    return min(prev1, prev2)
