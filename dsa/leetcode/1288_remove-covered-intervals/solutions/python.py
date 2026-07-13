def solve(intervals):
    intervals.sort(key=lambda item: (item[0], -item[1]))
    remaining = 0
    farthest_end = -1
    for _, end in intervals:
        if end > farthest_end:
            remaining += 1
            farthest_end = end
    return remaining
