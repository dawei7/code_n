from collections import Counter, defaultdict


class DetectSquares:
    def __init__(self):
        self.points: Counter[tuple[int, int]] = Counter()
        self.rows: defaultdict[int, Counter[int]] = defaultdict(Counter)

    def add(self, point: list[int]) -> None:
        x, y = point
        self.points[(x, y)] += 1
        self.rows[y][x] += 1

    def count(self, point: list[int]) -> int:
        x, y = point
        squares = 0

        for other_x, horizontal_count in self.rows[y].items():
            side = other_x - x
            if side == 0:
                continue
            squares += (
                horizontal_count
                * self.points[(x, y + side)]
                * self.points[(other_x, y + side)]
            )
            squares += (
                horizontal_count
                * self.points[(x, y - side)]
                * self.points[(other_x, y - side)]
            )

        return squares


def solve(operations: list[str], arguments: list[list[list[int]]]) -> list[int | None]:
    detector: DetectSquares | None = None
    output: list[int | None] = []

    for operation, args in zip(operations, arguments):
        if operation == "DetectSquares":
            detector = DetectSquares()
            output.append(None)
        elif operation == "add":
            assert detector is not None
            detector.add(args[0])
            output.append(None)
        elif operation == "count":
            assert detector is not None
            output.append(detector.count(args[0]))
        else:
            raise ValueError(f"unknown operation: {operation}")

    return output
