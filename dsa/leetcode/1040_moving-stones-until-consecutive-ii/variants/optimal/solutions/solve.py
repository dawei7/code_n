"""Optimal solution for LeetCode 1040: Moving Stones Until Consecutive II."""


def solve(stones: list[int]) -> list[int]:
    positions = sorted(stones)
    stone_count = len(positions)

    maximum_moves = max(
        positions[-1] - positions[1] - (stone_count - 2),
        positions[-2] - positions[0] - (stone_count - 2),
    )

    minimum_moves = stone_count
    left = 0
    for right, position in enumerate(positions):
        while position - positions[left] + 1 > stone_count:
            left += 1

        stones_in_window = right - left + 1
        consecutive_span = position - positions[left] + 1
        if stones_in_window == stone_count - 1 and consecutive_span == stone_count - 1:
            minimum_moves = min(minimum_moves, 2)
        else:
            minimum_moves = min(minimum_moves, stone_count - stones_in_window)

    return [minimum_moves, maximum_moves]
