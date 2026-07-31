from bisect import bisect_left, bisect_right


def solve(startTime: list[int], endTime: list[int]) -> int:
    sorted_starts = sorted(startTime)
    sorted_ends = sorted(endTime)

    answer = 1
    for start, end in zip(startTime, endTime):
        starting_by_end = bisect_right(sorted_starts, end)
        ending_before_start = bisect_left(sorted_ends, start)
        answer = max(answer, starting_by_end - ending_before_start)

    return answer
