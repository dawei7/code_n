class SubrectangleQueries:
    def __init__(self, rectangle):
        self.rectangle = [row[:] for row in rectangle]

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for row in range(row1, row2 + 1):
            for col in range(col1, col2 + 1):
                self.rectangle[row][col] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]


def solve(rectangle, operations):
    matrix = [list(row) for row in rectangle] if isinstance(rectangle, list) else [[rectangle]]
    if not matrix:
        matrix = [[0]]
    queries = SubrectangleQueries(matrix)
    output = []
    for raw_operation in operations:
        if not isinstance(raw_operation, list) or not raw_operation:
            continue
        name = str(raw_operation[0])
        args = raw_operation[1] if len(raw_operation) > 1 and isinstance(raw_operation[1], list) else []
        if name == "updateSubrectangle" and len(args) >= 5:
            row1, col1, row2, col2, value = map(int, args[:5])
            queries.updateSubrectangle(row1, col1, row2, col2, value)
            output.append(None)
        elif name == "getValue" and len(args) >= 2:
            row, col = map(int, args[:2])
            output.append(queries.getValue(row, col))
    return output
