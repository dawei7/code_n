def solve(events: list[list[int]]) -> int:
    answer = events[0][0]
    longest_duration = events[0][1]

    for position in range(1, len(events)):
        button, time = events[position]
        duration = time - events[position - 1][1]
        if duration > longest_duration or (duration == longest_duration and button < answer):
            longest_duration = duration
            answer = button

    return answer
