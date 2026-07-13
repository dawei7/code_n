def solve(schedule: list[list[list[int]]]) -> list[list[int]]:
    intervals = sorted(
        (interval for employee in schedule for interval in employee),
        key=lambda interval: interval[0],
    )

    free_time: list[list[int]] = []
    current_end = intervals[0][1]

    for start, end in intervals[1:]:
        if start > current_end:
            free_time.append([current_end, start])
        current_end = max(current_end, end)

    return free_time
