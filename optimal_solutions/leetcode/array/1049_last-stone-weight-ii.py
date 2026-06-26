"""Optimal solution for LeetCode 1049: Last Stone Weight II."""


def solve(stones: list[int]) -> int:
    total = sum(stones)
    possible = {0}
    for stone in stones:
        possible |= {value + stone for value in possible}
    best = max(value for value in possible if value <= total // 2)
    return total - 2 * best
