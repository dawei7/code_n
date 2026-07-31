from collections import defaultdict, deque


class Solution:
    def minMoves(self, matrix: list[str]) -> int:
        rows, columns = (len(matrix), len(matrix[0]))
        portals: dict[str, list[tuple[int, int]]] = defaultdict(list)
        for row in range(rows):
            for column in range(columns):
                cell = matrix[row][column]
                if cell.isalpha():
                    portals[cell].append((row, column))
        queue = deque([(0, 0, 0)])
        finalized: set[tuple[int, int]] = set()
        while queue:
            row, column, distance = queue.popleft()
            position = (row, column)
            if position in finalized:
                continue
            finalized.add(position)
            if position == (rows - 1, columns - 1):
                return distance
            cell = matrix[row][column]
            if cell.isalpha():
                for portal_row, portal_column in portals.pop(cell, []):
                    queue.appendleft((portal_row, portal_column, distance))
            for next_row, next_column in ((row - 1, column), (row + 1, column), (row, column - 1), (row, column + 1)):
                if 0 <= next_row < rows and 0 <= next_column < columns and (matrix[next_row][next_column] != "#"):
                    queue.append((next_row, next_column, distance + 1))
        return -1
