def solve(questions: list[list[int]]) -> int:
    count = len(questions)
    best = [0] * (count + 1)

    for index in range(count - 1, -1, -1):
        points, brainpower = questions[index]
        next_index = min(count, index + brainpower + 1)
        best[index] = max(best[index + 1], points + best[next_index])

    return best[0]
