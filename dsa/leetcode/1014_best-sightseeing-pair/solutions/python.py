"""Optimal solution for LeetCode 1014: Best Sightseeing Pair."""


def solve(values: list[int]) -> int:
    best_left = values[0]
    answer = 0
    for j in range(1, len(values)):
        answer = max(answer, best_left + values[j] - j)
        best_left = max(best_left, values[j] + j)
    return answer
