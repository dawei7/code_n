from bisect import bisect_left, bisect_right


def solve(flowers: list[list[int]], people: list[int]) -> list[int]:
    starts = sorted(start for start, _ in flowers)
    ends = sorted(end for _, end in flowers)
    return [bisect_right(starts, time) - bisect_left(ends, time) for time in people]
