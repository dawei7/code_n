def solve(intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
    result: list[list[int]] = []
    index = 0
    start, end = new_interval

    while index < len(intervals) and intervals[index][1] < start:
        result.append(intervals[index][:])
        index += 1

    while index < len(intervals) and intervals[index][0] <= end:
        start = min(start, intervals[index][0])
        end = max(end, intervals[index][1])
        index += 1

    result.append([start, end])
    result.extend(interval[:] for interval in intervals[index:])
    return result
