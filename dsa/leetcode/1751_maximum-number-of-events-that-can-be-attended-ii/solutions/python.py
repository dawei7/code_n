from bisect import bisect_right


def solve(events: list[list[int]], k: int) -> int:
    ordered = sorted(events)
    starts = [start for start, _, _ in ordered]
    next_index = [
        bisect_right(starts, end)
        for _, end, _ in ordered
    ]

    previous = [0] * (len(ordered) + 1)
    for _ in range(k):
        current = [0] * (len(ordered) + 1)
        for index in range(len(ordered) - 1, -1, -1):
            current[index] = max(
                current[index + 1],
                ordered[index][2] + previous[next_index[index]],
            )
        previous = current

    return previous[0]
