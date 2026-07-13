"""Greedy endpoint solution for LeetCode 452."""


def solve(points: list[list[int]]) -> int:
    if not points:
        return 0
    intervals = sorted(points, key=lambda interval: interval[1])
    arrows = 1
    arrow = intervals[0][1]
    for start, end in intervals[1:]:
        if start > arrow:
            arrows += 1
            arrow = end
    return arrows
