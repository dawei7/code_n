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
    left = 0
    right = reader.length() - 1

    while left < right:
        length = right - left + 1
        half = length // 2
        left_end = left + half - 1
        right_start = left + half
        right_end = right if length % 2 == 0 else right - 1
        comparison = reader.compareSub(left, left_end, right_start, right_end)
        if comparison > 0:
            right = left_end
        elif comparison < 0:
            left = right_start
            right = right_end
        else:
            return right
    return left
