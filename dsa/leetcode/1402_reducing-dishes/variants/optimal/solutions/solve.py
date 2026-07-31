"""Optimal app-local solution for LeetCode 1402: Reducing Dishes."""


def solve(satisfaction: list[int]) -> int:
    suffix_sum = 0
    coefficient = 0
    for value in sorted(satisfaction, reverse=True):
        if suffix_sum + value <= 0:
            break
        suffix_sum += value
        coefficient += suffix_sum
    return coefficient
