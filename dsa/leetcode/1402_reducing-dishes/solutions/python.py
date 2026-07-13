"""Optimal solution for LeetCode 1402: Reducing Dishes."""


def solve(satisfaction: list[int]) -> int:
    running = 0
    answer = 0
    for value in sorted(satisfaction, reverse=True):
        if running + value <= 0:
            break
        running += value
        answer += running
    return answer
