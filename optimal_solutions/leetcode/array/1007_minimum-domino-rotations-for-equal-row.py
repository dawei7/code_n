"""Optimal solution for LeetCode 1007: Minimum Domino Rotations For Equal Row."""


def solve(tops: list[int], bottoms: list[int]) -> int:
    def rotations(target: int) -> int:
        top_moves = 0
        bottom_moves = 0
        for top, bottom in zip(tops, bottoms):
            if top != target and bottom != target:
                return 10**9
            if top != target:
                top_moves += 1
            if bottom != target:
                bottom_moves += 1
        return min(top_moves, bottom_moves)

    best = min(rotations(tops[0]), rotations(bottoms[0]))
    return -1 if best == 10**9 else best
