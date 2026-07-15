def solve(intervals, to_be_removed):
    remove_start, remove_end = to_be_removed
    answer = []

    for start, end in intervals:
        if end <= remove_start or start >= remove_end:
            answer.append([start, end])
            continue
        if start < remove_start:
            answer.append([start, remove_start])
        if end > remove_end:
            answer.append([remove_end, end])

    return answer
