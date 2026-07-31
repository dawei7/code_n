class BinaryMatrix:
    """Local equivalent of LeetCode's read-only binary-matrix interface."""

    def __init__(self, matrix: list[list[int]]):
        self.matrix = matrix

    def get(self, row: int, col: int) -> int:
        return self.matrix[row][col]

    def dimensions(self) -> list[int]:
        return [len(self.matrix), len(self.matrix[0])]


def solve(binaryMatrix: BinaryMatrix) -> int:
    rows, cols = binaryMatrix.dimensions()
    row = 0
    col = cols - 1
    answer = -1
    while row < rows and col >= 0:
        if binaryMatrix.get(row, col) == 1:
            answer = col
            col -= 1
        else:
            row += 1
    return answer
