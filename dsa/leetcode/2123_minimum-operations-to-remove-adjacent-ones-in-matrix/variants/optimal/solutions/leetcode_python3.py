from collections import deque
from typing import Dict, List


class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        adjacency: Dict[int, List[int]] = {}

        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == 0 or (row + column) % 2:
                    continue
                vertex = row * columns + column
                neighbors = []
                for row_change, column_change in (
                    (-1, 0),
                    (1, 0),
                    (0, -1),
                    (0, 1),
                ):
                    next_row = row + row_change
                    next_column = column + column_change
                    if (
                        0 <= next_row < rows
                        and 0 <= next_column < columns
                        and grid[next_row][next_column] == 1
                    ):
                        neighbors.append(next_row * columns + next_column)
                adjacency[vertex] = neighbors

        pair_left = {vertex: -1 for vertex in adjacency}
        pair_right: Dict[int, int] = {}
        distance: Dict[int, int] = {}

        def build_layers() -> bool:
            queue = deque()
            for vertex in adjacency:
                if pair_left[vertex] == -1:
                    distance[vertex] = 0
                    queue.append(vertex)
                else:
                    distance[vertex] = -1

            found_augmenting = False
            while queue:
                vertex = queue.popleft()
                for neighbor in adjacency[vertex]:
                    mate = pair_right.get(neighbor, -1)
                    if mate == -1:
                        found_augmenting = True
                    elif distance[mate] == -1:
                        distance[mate] = distance[vertex] + 1
                        queue.append(mate)
            return found_augmenting

        def augment(vertex: int) -> bool:
            for neighbor in adjacency[vertex]:
                mate = pair_right.get(neighbor, -1)
                if mate == -1 or (
                    distance.get(mate) == distance[vertex] + 1
                    and augment(mate)
                ):
                    pair_left[vertex] = neighbor
                    pair_right[neighbor] = vertex
                    return True
            distance[vertex] = -1
            return False

        matching = 0
        while build_layers():
            for vertex in adjacency:
                if pair_left[vertex] == -1 and augment(vertex):
                    matching += 1

        return matching
