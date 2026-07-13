class NumMatrix:
    def __init__(self, matrix: list[list[int]]):
        rows = len(matrix)
        columns = len(matrix[0])
        self.prefix = [[0] * (columns + 1) for _ in range(rows + 1)]
        for row in range(rows):
            for column in range(columns):
                self.prefix[row + 1][column + 1] = (
                    matrix[row][column]
                    + self.prefix[row][column + 1]
                    + self.prefix[row + 1][column]
                    - self.prefix[row][column]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.prefix[row2 + 1][col2 + 1]
            - self.prefix[row1][col2 + 1]
            - self.prefix[row2 + 1][col1]
            + self.prefix[row1][col1]
        )
