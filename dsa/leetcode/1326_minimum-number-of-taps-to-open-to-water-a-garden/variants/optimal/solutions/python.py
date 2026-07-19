"""Optimal app-local solution for LeetCode 1326."""


def solve(n, ranges):
    farthest = [0] * (n + 1)
    for position, radius in enumerate(ranges):
        left = max(0, position - radius)
        right = min(n, position + radius)
        farthest[left] = max(farthest[left], right)

    taps = 0
    current_end = 0
    next_end = 0
    for position in range(n):
        next_end = max(next_end, farthest[position])
        if position == current_end:
            if next_end <= position:
                return -1
            taps += 1
            current_end = next_end
    return taps
