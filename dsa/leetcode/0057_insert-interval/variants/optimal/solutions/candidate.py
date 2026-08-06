def solve(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    result: list[list[int]] = []
    i = 0
    start, end = newInterval

    while i < len(intervals) and intervals[i][1] < start:
        result.append(intervals[i][:])
        i += 1

    while i < len(intervals) and intervals[i][0] <= end:
        start = min(start, intervals[i][0])
        end = max(end, intervals[i][1])
        i += 1

    result.append([start, end])
    result.extend(interval[:] for interval in intervals[i:])
    return result
