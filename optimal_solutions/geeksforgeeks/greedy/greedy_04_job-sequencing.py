"""Optimal solution for greedy_04: Job Sequencing.

Auto-generated from challenges/algorithms/greedy.py:SPECS.
O(n²) time.
"""


def solve(deadline, profit, n):
    # Build job tuples and sort by profit descending.
    jobs = sorted(
        ((profit[i], deadline[i]) for i in range(n)),
        key=lambda j: j[0],
        reverse=True,
    )
    # latest_free[t] is the latest time slot that is still available
    # up to t. We collapse the search with a simple boolean array.
    slots = [False] * (n + 1)
    total = 0
    for p, d in jobs:
        # Find the latest free slot <= min(d, n).
        for t in range(min(d, n), 0, -1):
            if not slots[t]:
                slots[t] = True
                total += p
                break
    return total
