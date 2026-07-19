def solve(intervals):
    ordered = sorted(intervals, key=lambda interval: (interval[0], -interval[1]))
    remaining = 0
    farthest_right = -1
    for _, right in ordered:
        if right > farthest_right:
            remaining += 1
            farthest_right = right
    return remaining
