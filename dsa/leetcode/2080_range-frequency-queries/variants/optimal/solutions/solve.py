from bisect import bisect_left, bisect_right
from collections import defaultdict


class RangeFreqQuery:
    def __init__(self, arr: list[int]):
        self.positions = defaultdict(list)
        for index, value in enumerate(arr):
            self.positions[value].append(index)

    def query(self, left: int, right: int, value: int) -> int:
        positions = self.positions[value]
        return bisect_right(positions, right) - bisect_left(positions, left)


def solve(operations: list[str], arguments: list[list[object]]) -> list[int | None]:
    frequency_query: RangeFreqQuery | None = None
    output: list[int | None] = []

    for operation, args in zip(operations, arguments):
        if operation == "RangeFreqQuery":
            frequency_query = RangeFreqQuery(args[0])
            output.append(None)
        elif operation == "query":
            assert frequency_query is not None
            output.append(frequency_query.query(args[0], args[1], args[2]))
        else:
            raise ValueError(f"unknown operation: {operation}")

    return output
