from functools import lru_cache
from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        cells = []
        start = -1
        end = -1

        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == -1:
                    continue
                index = len(cells)
                cells.append((row, column))
                if grid[row][column] == 1:
                    start = index
                elif grid[row][column] == 2:
                    end = index

        index_by_cell = {cell: index for index, cell in enumerate(cells)}
        neighbors = []
        for row, column in cells:
            adjacent = []
            for candidate in (
                (row + 1, column),
                (row - 1, column),
                (row, column + 1),
                (row, column - 1),
            ):
                if candidate in index_by_cell:
                    adjacent.append(index_by_cell[candidate])
            neighbors.append(adjacent)

        full_mask = (1 << len(cells)) - 1

        @lru_cache(maxsize=None)
        def count(position, visited):
            if position == end:
                return int(visited == full_mask)
            total = 0
            for neighbor in neighbors[position]:
                bit = 1 << neighbor
                if visited & bit == 0:
                    total += count(neighbor, visited | bit)
            return total

        return count(start, 1 << start)
