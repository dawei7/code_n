"""Optimal app-local solution for LeetCode 1014."""


def solve(values):
    best_left = values[0]
    answer = 0

    for index in range(1, len(values)):
        answer = max(answer, best_left + values[index] - index)
        best_left = max(best_left, values[index] + index)

    return answer
