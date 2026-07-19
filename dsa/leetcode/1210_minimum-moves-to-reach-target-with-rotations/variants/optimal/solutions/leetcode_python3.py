from collections import deque
from typing import List


class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        target = (n - 1, n - 2, 0)
        queue = deque([(0, 0, 0, 0)])
        seen = {(0, 0, 0)}
        while queue:
            row, column, orientation, moves = queue.popleft()
            if (row, column, orientation) == target:
                return moves
            if orientation == 0:
                if column + 2 < n and grid[row][column + 2] == 0:
                    state = (row, column + 1, 0)
                    if state not in seen:
                        seen.add(state)
                        queue.append((*state, moves + 1))
                if row + 1 < n and grid[row + 1][column] == 0 and grid[row + 1][column + 1] == 0:
                    for state in ((row + 1, column, 0), (row, column, 1)):
                        if state not in seen:
                            seen.add(state)
                            queue.append((*state, moves + 1))
            else:
                if row + 2 < n and grid[row + 2][column] == 0:
                    state = (row + 1, column, 1)
                    if state not in seen:
                        seen.add(state)
                        queue.append((*state, moves + 1))
                if column + 1 < n and grid[row][column + 1] == 0 and grid[row + 1][column + 1] == 0:
                    for state in ((row, column + 1, 1), (row, column, 0)):
                        if state not in seen:
                            seen.add(state)
                            queue.append((*state, moves + 1))
        return -1
