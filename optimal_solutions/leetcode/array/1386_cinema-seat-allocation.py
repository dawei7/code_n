"""Optimal solution for LeetCode 1386: Cinema Seat Allocation."""

from collections import defaultdict


def solve(n: int, reserved_seats: list[list[int]]) -> int:
    occupied: dict[int, int] = defaultdict(int)
    for row, seat in reserved_seats:
        if 2 <= seat <= 9:
            occupied[row] |= 1 << seat

    answer = (n - len(occupied)) * 2
    left = sum(1 << seat for seat in range(2, 6))
    middle = sum(1 << seat for seat in range(4, 8))
    right = sum(1 << seat for seat in range(6, 10))

    for mask in occupied.values():
        can_left = mask & left == 0
        can_right = mask & right == 0
        if can_left and can_right:
            answer += 2
        elif can_left or can_right or mask & middle == 0:
            answer += 1
    return answer
