"""Optimal app-local solution for LeetCode 1024."""


def solve(clips, time):
    farthest_from_start = [0] * (time + 1)
    for start, end in clips:
        if start <= time:
            farthest_from_start[start] = max(farthest_from_start[start], end)

    used = 0
    current_end = 0
    farthest = 0
    for position in range(time):
        farthest = max(farthest, farthest_from_start[position])
        if farthest <= position:
            return -1
        if position == current_end:
            used += 1
            current_end = farthest
            if current_end >= time:
                return used

    return used
