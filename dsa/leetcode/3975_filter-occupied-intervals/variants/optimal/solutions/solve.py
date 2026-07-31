def solve(
    occupiedIntervals: list[list[int]],
    freeStart: int,
    freeEnd: int,
) -> list[list[int]]:
    merged: list[list[int]] = []
    for start, end in sorted(occupiedIntervals):
        if not merged or start > merged[-1][1] + 1:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)

    answer: list[list[int]] = []
    for start, end in merged:
        if end < freeStart or start > freeEnd:
            answer.append([start, end])
            continue
        if start < freeStart:
            answer.append([start, freeStart - 1])
        if end > freeEnd:
            answer.append([freeEnd + 1, end])
    return answer
