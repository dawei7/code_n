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


class Solution:
    def search(self, reader: ArrayReader, target: int) -> int:
        left = 0
        right = 1

        while reader.get(right) < target:
            left = right + 1
            right *= 2

        while left <= right:
            middle = (left + right) // 2
            value = reader.get(middle)
            if value == target:
                return middle
            if value < target:
                left = middle + 1
            else:
                right = middle - 1

        return -1


def solve(reader: list[int], target: int) -> int:
    return Solution().search(ArrayReader(reader), target)
