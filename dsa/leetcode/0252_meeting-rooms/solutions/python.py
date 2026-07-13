def solve(intervals: list[list[int]]) -> bool:
    ordered = sorted(intervals)
    return all(ordered[i - 1][1] <= ordered[i][0] for i in range(1, len(ordered)))
