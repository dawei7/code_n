def solve(s: str) -> int:
    occupied = 0
    answer = 0

    for event in s:
        if event == "E":
            occupied += 1
            answer = max(answer, occupied)
        else:
            occupied -= 1

    return answer
