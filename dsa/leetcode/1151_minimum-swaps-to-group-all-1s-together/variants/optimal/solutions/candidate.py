"""Proposed app-local solution for LeetCode 1151."""


def solve(data: list[int]) -> int:
    ones = sum(data)
    if ones <= 1:
        return 0

    zeros_in_window = sum(1 - data[position] for position in range(ones))
    minimum_swaps = zeros_in_window
    for right in range(ones, len(data)):
        zeros_in_window += data[right - ones] - data[right]
        minimum_swaps = min(minimum_swaps, zeros_in_window)
    return minimum_swaps
