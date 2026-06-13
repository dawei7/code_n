"""Optimal solution for dp_22: Egg Dropping.

Return the minimum number of trials needed in the worst
case to find the critical floor. dp[e][f] = min trials for
e eggs and f floors. Drop from floor x -> 1 + worst(
dp[e-1][x-1], dp[e][f-x]).
"""


def solve(eggs, floors):
    if floors == 0:
        return 0
    if eggs == 1:
        return floors
    dp = [[0] * (floors + 1) for _ in range(eggs + 1)]
    for f in range(1, floors + 1):
        dp[1][f] = f
    for e in range(2, eggs + 1):
        for f in range(1, floors + 1):
            best = f
            for x in range(1, f + 1):
                worst = 1 + max(dp[e - 1][x - 1], dp[e][f - x])
                if worst < best:
                    best = worst
            dp[e][f] = best
    return dp[eggs][floors]
