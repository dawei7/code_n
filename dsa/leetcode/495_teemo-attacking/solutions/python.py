"""Capped-gap interval-union scan for LeetCode 495."""


def solve(time_series: list[int], duration: int) -> int:
    if not time_series:
        return 0
    total = duration
    for index in range(len(time_series) - 1):
        total += min(duration, time_series[index + 1] - time_series[index])
    return total
