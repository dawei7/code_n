def solve(intervals: list[list[int]], k: int) -> int:
    intervals.sort()
    merged = []

    for start, end in intervals:
        if merged and start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])

    left = 0
    most_joined = 1

    for right in range(len(merged)):
        while merged[right][0] - merged[left][1] > k:
            left += 1
        most_joined = max(most_joined, right - left + 1)

    return len(merged) - most_joined + 1
