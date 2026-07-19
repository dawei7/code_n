from collections import deque
from typing import List


class Solution:
    def isEscapePossible(
        self, blocked: List[List[int]], source: List[int], target: List[int]
    ) -> bool:
        grid_size = 1_000_000
        blocked_set = {tuple(cell) for cell in blocked}
        enclosure_limit = len(blocked) * (len(blocked) - 1) // 2

        def escapes(start, finish):
            queue = deque([start])
            seen = {start}
            while queue and len(seen) <= enclosure_limit:
                row, col = queue.popleft()
                if (row, col) == finish:
                    return True
                for row_step, col_step in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    next_row = row + row_step
                    next_col = col + col_step
                    next_cell = (next_row, next_col)
                    if (
                        0 <= next_row < grid_size
                        and 0 <= next_col < grid_size
                        and next_cell not in blocked_set
                        and next_cell not in seen
                    ):
                        seen.add(next_cell)
                        queue.append(next_cell)
            return len(seen) > enclosure_limit

        source_cell = tuple(source)
        target_cell = tuple(target)
        return escapes(source_cell, target_cell) and escapes(target_cell, source_cell)

