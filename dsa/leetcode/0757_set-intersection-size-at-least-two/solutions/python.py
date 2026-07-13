def solve(intervals: list[list[int]]) -> int:
    intervals.sort(key=lambda interval: (interval[1], -interval[0]))

    left = -1
    right = -1
    selected_count = 0

    for start, end in intervals:
        if start > right:
            selected_count += 2
            left = end - 1
            right = end
        elif start > left:
            selected_count += 1
            left = right
            right = end

    return selected_count
