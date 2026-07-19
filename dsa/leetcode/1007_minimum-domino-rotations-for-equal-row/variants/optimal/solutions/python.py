"""Optimal app-local solution for LeetCode 1007."""


def solve(tops, bottoms):
    def rotations(target):
        top_moves = 0
        bottom_moves = 0

        for top, bottom in zip(tops, bottoms):
            if top != target and bottom != target:
                return None
            if top != target:
                top_moves += 1
            if bottom != target:
                bottom_moves += 1

        return min(top_moves, bottom_moves)

    results = (rotations(tops[0]), rotations(bottoms[0]))
    feasible = [result for result in results if result is not None]
    return min(feasible) if feasible else -1
