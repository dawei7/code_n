"""Consistent-turn cross-product solution for LeetCode 469."""


def solve(points: list[list[int]]) -> bool:
    orientation = 0
    count = len(points)
    for i in range(count):
        first = points[i]
        second = points[(i + 1) % count]
        third = points[(i + 2) % count]
        cross = (second[0] - first[0]) * (third[1] - second[1]) - (second[1] - first[1]) * (third[0] - second[0])
        if cross == 0:
            continue
        if orientation and (cross > 0) != (orientation > 0):
            return False
        orientation = cross
    return True
