"""Two-dimensional Fenwick tree for LeetCode 308."""


class NumMatrix:
    def __init__(self, matrix: list[list[int]]):
        self.rows = len(matrix)
        self.columns = len(matrix[0]) if matrix else 0
        self.values = [row[:] for row in matrix]
        self.tree = [
            [0] * (self.columns + 1) for _ in range(self.rows + 1)
        ]
        for row in range(self.rows):
            for column in range(self.columns):
                self._add(row, column, matrix[row][column])

    def _add(self, row: int, column: int, delta: int) -> None:
        row_index = row + 1
        while row_index <= self.rows:
            column_index = column + 1
            while column_index <= self.columns:
                self.tree[row_index][column_index] += delta
                column_index += column_index & -column_index
            row_index += row_index & -row_index

    def update(self, row: int, col: int, val: int) -> None:
        delta = val - self.values[row][col]
        self.values[row][col] = val
        self._add(row, col, delta)

    def _prefix_sum(self, row: int, column: int) -> int:
        total = 0
        row_index = row + 1
        while row_index > 0:
            column_index = column + 1
            while column_index > 0:
                total += self.tree[row_index][column_index]
                column_index -= column_index & -column_index
            row_index -= row_index & -row_index
        return total

    def sumRegion(
        self, row1: int, col1: int, row2: int, col2: int
    ) -> int:
        return (
            self._prefix_sum(row2, col2)
            - self._prefix_sum(row1 - 1, col2)
            - self._prefix_sum(row2, col1 - 1)
            + self._prefix_sum(row1 - 1, col1 - 1)
        )


def solve(matrix: list[list[int]], operations: list[list[int | str]]) -> list[int]:
    query_matrix = NumMatrix(matrix)
    result: list[int] = []
    for operation in operations:
        if operation[0] == "update":
            query_matrix.update(operation[1], operation[2], operation[3])
        else:
            result.append(query_matrix.sumRegion(*operation[1:]))
    return result
