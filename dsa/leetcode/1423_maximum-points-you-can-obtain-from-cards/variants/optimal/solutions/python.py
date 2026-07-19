"""Optimal app-local solution for LeetCode 1423."""


def solve(card_points: list[int], k: int) -> int:
    total = sum(card_points)
    remaining_length = len(card_points) - k
    if remaining_length == 0:
        return total

    remaining_sum = sum(card_points[:remaining_length])
    minimum_remaining = remaining_sum
    for right in range(remaining_length, len(card_points)):
        remaining_sum += card_points[right] - card_points[right - remaining_length]
        minimum_remaining = min(minimum_remaining, remaining_sum)
    return total - minimum_remaining
