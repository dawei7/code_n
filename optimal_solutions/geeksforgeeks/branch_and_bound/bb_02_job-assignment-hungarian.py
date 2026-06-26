"""Optimal solution for bb_02: Job Assignment.

Given an n x n cost matrix cost[i][j] = cost to assign job j
to worker i, find the minimum-cost assignment. Brute-force
enumerate all n! permutations of jobs. Setup keeps n small
(n <= 6) so this is tractable.
"""


def solve(cost, n):
    if n == 0:
        return 0
    jobs = list(range(n))
    best = float("inf")

    def helper(worker, used, current):
        nonlocal best
        if worker == n:
            if current < best:
                best = current
            return
        for job in jobs:
            if not used[job]:
                used[job] = True
                helper(worker + 1, used, current + cost[worker][job])
                used[job] = False

    helper(0, [False] * n, 0)
    return best
