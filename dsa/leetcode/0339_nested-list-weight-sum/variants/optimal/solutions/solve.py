class NestedInteger:
    """Local equivalent of LeetCode's read-only NestedInteger interface."""

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
    def weighted_sum(values: list[NestedInteger], depth: int) -> int:
        total = 0
        for value in values:
            if value.isInteger():
                total += value.getInteger() * depth
            else:
                total += weighted_sum(value.getList(), depth + 1)
        return total

    return weighted_sum(nestedList, 1)
