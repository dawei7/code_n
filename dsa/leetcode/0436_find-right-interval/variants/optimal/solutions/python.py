"""Optimal app-local solution for LeetCode 436."""

from bisect import bisect_left


def solve(intervals: list[list[int]]) -> list[int]:
    indexed_starts = sorted((start, index) for index, (start, _) in enumerate(intervals))
    starts = [start for start, _ in indexed_starts]
    answer: list[int] = []
    for _, end in intervals:
        position = bisect_left(starts, end)
        answer.append(-1 if position == len(starts) else indexed_starts[position][1])
    return answer
