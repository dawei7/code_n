class ArrayReader:
    """Local equivalent of LeetCode's ArrayReader for the standalone app."""

    def __init__(self, values: list[int]):
        self.values = values

    def get(self, index: int) -> int:
        return self.values[index] if index < len(self.values) else 2**31 - 1

    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
        first = sum(self.values[l : r + 1])
        second = sum(self.values[x : y + 1])
        return (first > second) - (first < second)

    def length(self) -> int:
        return len(self.values)

    def query(self, a: int, b: int, c: int, d: int) -> int:
        ones = sum(self.values[index] for index in (a, b, c, d))
        return 4 if ones in (0, 4) else 2 if ones in (1, 3) else 0


def solve(reader):
    n = reader.length()
    baseline = reader.query(0, 1, 2, 3)
    comparison = reader.query(0, 1, 2, 4)

    same = 1
    different = 0
    different_index = -1

    if comparison == baseline:
        same += 1
    else:
        different += 1
        different_index = 4

    for index in range(5, n):
        if reader.query(0, 1, 2, index) == baseline:
            same += 1
        else:
            different += 1
            different_index = index

    checks = (
        (reader.query(0, 1, 3, 4), 2),
        (reader.query(0, 2, 3, 4), 1),
        (reader.query(1, 2, 3, 4), 0),
    )
    for result, index in checks:
        if result == comparison:
            same += 1
        else:
            different += 1
            different_index = index

    if same == different:
        return -1
    return 3 if same > different else different_index
