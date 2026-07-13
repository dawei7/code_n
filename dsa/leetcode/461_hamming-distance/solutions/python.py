"""XOR population-count solution for LeetCode 461."""


def solve(x: int, y: int) -> int:
    difference = x ^ y
    distance = 0
    while difference:
        difference &= difference - 1
        distance += 1
    return distance
