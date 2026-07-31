from typing import List


def solve(peaks: List[List[int]]) -> int:
    ranges = sorted(
        ((x - y, x + y) for x, y in peaks),
        key=lambda interval: (interval[0], -interval[1]),
    )
    visible = 0
    rightmost = -1

    for index, interval in enumerate(ranges):
        duplicate = (
            (index > 0 and ranges[index - 1] == interval)
            or (index + 1 < len(ranges) and ranges[index + 1] == interval)
        )
        if not duplicate and interval[1] > rightmost:
            visible += 1
        rightmost = max(rightmost, interval[1])

    return visible
