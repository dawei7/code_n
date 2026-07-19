"""Optimal app-local solution for LeetCode 849."""


def solve(seats):
    best = 0
    previous = -1

    for index, occupied in enumerate(seats):
        if occupied == 0:
            continue
        if previous < 0:
            best = index
        else:
            best = max(best, (index - previous) // 2)
        previous = index

    return max(best, len(seats) - 1 - previous)
