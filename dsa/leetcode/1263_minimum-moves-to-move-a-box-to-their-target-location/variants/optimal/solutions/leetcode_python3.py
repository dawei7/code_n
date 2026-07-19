from collections import deque
from typing import List


class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        rows, columns = len(grid), len(grid[0])
        box = player = target = None
        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == "B": box = (row, column)
                elif grid[row][column] == "S": player = (row, column)
                elif grid[row][column] == "T": target = (row, column)

        def free(cell, blocked_box):
            row, column = cell
            return 0 <= row < rows and 0 <= column < columns and grid[row][column] != "#" and cell != blocked_box

        def can_reach(start, goal, blocked_box):
            queue = deque([start])
            seen = {start}
            while queue:
                row, column = queue.popleft()
                if (row, column) == goal:
                    return True
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nxt = (row + dr, column + dc)
                    if nxt not in seen and free(nxt, blocked_box):
                        seen.add(nxt)
                        queue.append(nxt)
            return False

        queue = deque([(box, player, 0)])
        seen = {(box, player)}
        while queue:
            current_box, current_player, pushes = queue.popleft()
            if current_box == target:
                return pushes
            row, column = current_box
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                stand = (row - dr, column - dc)
                destination = (row + dr, column + dc)
                if not free(destination, current_box) or not free(stand, current_box):
                    continue
                if not can_reach(current_player, stand, current_box):
                    continue
                state = (destination, current_box)
                if state not in seen:
                    seen.add(state)
                    queue.append((destination, current_box, pushes + 1))
        return -1
