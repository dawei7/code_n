from typing import List


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def build(row: int, column: int, size: int) -> 'Node':
            if size == 1:
                return Node(bool(grid[row][column]), True)

            half = size // 2
            top_left = build(row, column, half)
            top_right = build(row, column + half, half)
            bottom_left = build(row + half, column, half)
            bottom_right = build(row + half, column + half, half)
            children = (top_left, top_right, bottom_left, bottom_right)

            if all(child.isLeaf and child.val == top_left.val for child in children):
                return Node(top_left.val, True)
            return Node(True, False, top_left, top_right, bottom_left, bottom_right)

        return build(0, 0, len(grid))
