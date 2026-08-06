class ArrayReader:
    """Local equivalent of LeetCode's ArrayReader for the standalone app."""

    def __init__(self, values: list[int]):
        self.values = values

    def get(self, position: int) -> int:
        return self.values[position] if position < len(self.values) else 2**31 - 1


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
