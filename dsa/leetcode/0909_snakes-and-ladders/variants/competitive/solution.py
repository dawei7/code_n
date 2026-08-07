from collections import deque
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        size = len(board)
        cells = [-1]
        left_to_right = True
        for row in range(size - 1, -1, -1):
            columns = range(size) if left_to_right else range(size - 1, -1, -1)
            for column in columns:
                cells.append(board[row][column])
            left_to_right = not left_to_right

        target = size * size
        queue = deque([(1, 0)])
        visited = {1}

        while queue:
            current, rolls = queue.popleft()
            for next_square in range(current + 1, min(current + 6, target) + 1):
                destination = cells[next_square] if cells[next_square] != -1 else next_square
                if destination == target:
                    return rolls + 1
                if destination not in visited:
                    visited.add(destination)
                    queue.append((destination, rolls + 1))

        return -1
