from collections import deque
from typing import List


class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        columns = len(mat[0])
        start = 0
        for row in range(rows):
            for column in range(columns):
                if mat[row][column]:
                    start |= 1 << (row * columns + column)

        if start == 0:
            return 0

        flip_masks = []
        for row in range(rows):
            for column in range(columns):
                flip_mask = 0
                for row_delta, column_delta in ((0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)):
                    next_row = row + row_delta
                    next_column = column + column_delta
                    if 0 <= next_row < rows and 0 <= next_column < columns:
                        flip_mask ^= 1 << (next_row * columns + next_column)
                flip_masks.append(flip_mask)

        queue = deque([(start, 0)])
        seen = {start}
        while queue:
            state, steps = queue.popleft()
            for flip_mask in flip_masks:
                next_state = state ^ flip_mask
                if next_state == 0:
                    return steps + 1
                if next_state not in seen:
                    seen.add(next_state)
                    queue.append((next_state, steps + 1))

        return -1
