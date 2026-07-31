"""Optimal app-local solution for LeetCode 364."""


class NestedInteger:
    """Local equivalent of LeetCode's NestedInteger interface."""

    def __init__(self, value: int | list["NestedInteger"] | None = None):
        if isinstance(value, int):
            self._integer = value
            self._list = None
        else:
            self._integer = None
            self._list = [] if value is None else value

    def isInteger(self) -> bool:
        return self._integer is not None

    def getInteger(self) -> int | None:
        return self._integer

    def add(self, element: "NestedInteger") -> None:
        if self._list is None:
            self._integer = None
            self._list = []
        self._list.append(element)

    def setInteger(self, value: int) -> None:
        self._integer = value
        self._list = None

    def getList(self) -> list["NestedInteger"] | None:
        return self._list


def solve(nestedList: list[NestedInteger]) -> int:
    depth_sums = []
    maximum_integer_depth = 0

    def collect(values: list[NestedInteger], depth: int) -> None:
        nonlocal maximum_integer_depth
        for value in values:
            if value.isInteger():
                while len(depth_sums) < depth:
                    depth_sums.append(0)
                depth_sums[depth - 1] += value.getInteger()
                maximum_integer_depth = max(maximum_integer_depth, depth)
            else:
                collect(value.getList(), depth + 1)

    collect(nestedList, 1)
    return sum(depth_sum * (maximum_integer_depth - depth + 1) for depth, depth_sum in enumerate(depth_sums, start=1))
