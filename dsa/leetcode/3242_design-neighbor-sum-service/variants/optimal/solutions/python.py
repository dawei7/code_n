class NeighborSum:
    def __init__(self, grid: list[list[int]]):
        side = len(grid)
        value_count = side * side
        self.adjacent = [0] * value_count
        self.diagonal = [0] * value_count

        adjacent_directions = ((-1, 0), (0, -1), (0, 1), (1, 0))
        diagonal_directions = ((-1, -1), (-1, 1), (1, -1), (1, 1))

        for row in range(side):
            for column in range(side):
                value = grid[row][column]
                for row_change, column_change in adjacent_directions:
                    neighbor_row = row + row_change
                    neighbor_column = column + column_change
                    if 0 <= neighbor_row < side and 0 <= neighbor_column < side:
                        self.adjacent[value] += grid[neighbor_row][neighbor_column]

                for row_change, column_change in diagonal_directions:
                    neighbor_row = row + row_change
                    neighbor_column = column + column_change
                    if 0 <= neighbor_row < side and 0 <= neighbor_column < side:
                        self.diagonal[value] += grid[neighbor_row][neighbor_column]

    def adjacentSum(self, value: int) -> int:
        return self.adjacent[value]

    def diagonalSum(self, value: int) -> int:
        return self.diagonal[value]


def solve(operations: list[str], arguments: list[list[object]]) -> list[int | None]:
    service: NeighborSum | None = None
    output: list[int | None] = []

    for operation, args in zip(operations, arguments):
        if operation == "NeighborSum":
            service = NeighborSum(args[0])
            output.append(None)
        elif operation == "adjacentSum":
            assert service is not None
            output.append(service.adjacentSum(args[0]))
        elif operation == "diagonalSum":
            assert service is not None
            output.append(service.diagonalSum(args[0]))
        else:
            raise ValueError(f"unknown operation: {operation}")

    return output
