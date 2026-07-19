"""Reference solution for LeetCode 1386."""


from collections import defaultdict


LEFT_BLOCK = sum(1 << seat for seat in range(2, 6))
MIDDLE_BLOCK = sum(1 << seat for seat in range(4, 8))
RIGHT_BLOCK = sum(1 << seat for seat in range(6, 10))


def solve(n: int, reserved_seats: list[list[int]]) -> int:
    occupied: dict[int, int] = defaultdict(int)
    for row, seat in reserved_seats:
        if 2 <= seat <= 9:
            occupied[row] |= 1 << seat

    families = 2 * (n - len(occupied))
    for mask in occupied.values():
        left_free = mask & LEFT_BLOCK == 0
        right_free = mask & RIGHT_BLOCK == 0
        if left_free and right_free:
            families += 2
        elif left_free or right_free or mask & MIDDLE_BLOCK == 0:
            families += 1

    return families
