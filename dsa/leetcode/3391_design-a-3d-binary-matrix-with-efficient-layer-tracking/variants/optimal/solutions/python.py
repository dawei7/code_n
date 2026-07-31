from heapq import heapify, heappop, heappush


class Matrix3D:
    def __init__(self, n: int):
        self.cells = set()
        self.layer_counts = [0] * n
        self.layers = [(0, -x) for x in range(n)]
        heapify(self.layers)

    def setCell(self, x: int, y: int, z: int) -> None:
        cell = (x, y, z)
        if cell in self.cells:
            return

        self.cells.add(cell)
        self.layer_counts[x] += 1
        heappush(self.layers, (-self.layer_counts[x], -x))

    def unsetCell(self, x: int, y: int, z: int) -> None:
        cell = (x, y, z)
        if cell not in self.cells:
            return

        self.cells.remove(cell)
        self.layer_counts[x] -= 1
        heappush(self.layers, (-self.layer_counts[x], -x))

    def largestMatrix(self) -> int:
        while -self.layers[0][0] != self.layer_counts[-self.layers[0][1]]:
            heappop(self.layers)
        return -self.layers[0][1]


def solve(operations: list[str], arguments: list[list[int]]) -> list[int | None]:
    matrix: Matrix3D | None = None
    output: list[int | None] = []

    for operation, args in zip(operations, arguments):
        if operation == "Matrix3D":
            matrix = Matrix3D(args[0])
            output.append(None)
        elif operation == "setCell":
            assert matrix is not None
            matrix.setCell(*args)
            output.append(None)
        elif operation == "unsetCell":
            assert matrix is not None
            matrix.unsetCell(*args)
            output.append(None)
        elif operation == "largestMatrix":
            assert matrix is not None
            output.append(matrix.largestMatrix())
        else:
            raise ValueError(f"unknown operation: {operation}")

    return output
