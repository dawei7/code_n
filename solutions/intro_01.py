"""Optimal solution for intro_01: Hello Grid.

Find the maximum value in a list-like input. O(n) solution.
"""


def solve(data):
    """Iterate once, track the running maximum."""
    n = len(data)
    best = data[0]
    for i in range(1, n):
        value = data[i]
        if value > best:
            best = value
    return best
