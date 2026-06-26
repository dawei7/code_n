"""Optimal solution for greedy_01: Activity Selection.

Auto-generated from challenges/algorithms/greedy.py:SPECS.
O(n log n) time.
"""


def solve(start, finish, n):
    pairs = sorted(zip(start, finish), key=lambda p: p[1])
    if not pairs:
        return 0
    count = 1
    last_finish = pairs[0][1]
    for s, f in pairs[1:]:
        if s >= last_finish:
            count += 1
            last_finish = f
    return count
