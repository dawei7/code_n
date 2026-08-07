class Solution:
    def findPath(self, grid: list[list[int]], k: int) -> list[list[int]]:
        rows = len(grid)
        columns = len(grid[0])
        total_cells = rows * columns
        visited = [[False] * columns for _ in range(rows)]
        path: list[list[int]] = []

        def search(row: int, column: int, next_checkpoint: int) -> list[list[int]] | None:
            checkpoint = grid[row][column]
            if checkpoint != 0:
                if checkpoint != next_checkpoint:
                    return None
                next_checkpoint += 1
            visited[row][column] = True
            path.append([row, column])
            if len(path) == total_cells:
                return [position[:] for position in path]
            for next_row, next_column in ((row + 1, column), (row - 1, column), (row, column + 1), (row, column - 1)):
                if 0 <= next_row < rows and 0 <= next_column < columns and (not visited[next_row][next_column]):
                    answer = search(next_row, next_column, next_checkpoint)
                    if answer is not None:
                        return answer
            path.pop()
            visited[row][column] = False
            return None

        for start_row in range(rows):
            for start_column in range(columns):
                answer = search(start_row, start_column, 1)
                if answer is not None:
                    return answer
        return []
