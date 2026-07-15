"""Optimal app-local solution for LeetCode 881."""


def solve(people, limit):
    weights = sorted(people)
    light = 0
    heavy = len(weights) - 1
    boats = 0

    while light <= heavy:
        if weights[light] + weights[heavy] <= limit:
            light += 1
        heavy -= 1
        boats += 1

    return boats
