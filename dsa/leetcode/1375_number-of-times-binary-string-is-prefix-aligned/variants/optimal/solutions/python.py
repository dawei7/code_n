"""Reference solution for LeetCode 1375."""


def solve(flips: list[int]) -> int:
    aligned = 0
    rightmost = 0

    for step, position in enumerate(flips, start=1):
        rightmost = max(rightmost, position)
        if rightmost == step:
            aligned += 1

    return aligned
