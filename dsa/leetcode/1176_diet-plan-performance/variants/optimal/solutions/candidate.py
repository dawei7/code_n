"""Proposed app-local solution for LeetCode 1176."""


def solve(calories: list[int], k: int, lower: int, upper: int) -> int:
    window_sum = sum(calories[position] for position in range(k))
    score = 0

    if window_sum < lower:
        score -= 1
    elif window_sum > upper:
        score += 1

    for right in range(k, len(calories)):
        window_sum += calories[right] - calories[right - k]
        if window_sum < lower:
            score -= 1
        elif window_sum > upper:
            score += 1

    return score
