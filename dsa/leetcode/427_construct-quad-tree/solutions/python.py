"""Optimal app-local solution for LeetCode 427."""

from types import SimpleNamespace


def solve(grid: list[list[int]]):
    def leaf(value: int):
        return SimpleNamespace(
            val=bool(value),
            isLeaf=True,
            topLeft=None,
            topRight=None,
            bottomLeft=None,
            bottomRight=None,
        )

    def build(row: int, column: int, size: int):
        if size == 1:
            return leaf(grid[row][column])

        half = size // 2
        top_left = build(row, column, half)
        top_right = build(row, column + half, half)
        bottom_left = build(row + half, column, half)
        bottom_right = build(row + half, column + half, half)
        children = (top_left, top_right, bottom_left, bottom_right)

        if all(child.isLeaf and child.val == top_left.val for child in children):
            return leaf(int(top_left.val))
        return SimpleNamespace(
            val=True,
            isLeaf=False,
            topLeft=top_left,
            topRight=top_right,
            bottomLeft=bottom_left,
            bottomRight=bottom_right,
        )

    return build(0, 0, len(grid))
