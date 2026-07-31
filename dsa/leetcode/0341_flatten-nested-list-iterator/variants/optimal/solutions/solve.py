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


class NestedIterator:
    def __init__(self, nestedList: list[NestedInteger]):
        self.stack = [iter(nestedList)]
        self.cached = None
        self.ready = False

    def next(self) -> int:
        if not self.hasNext():
            raise StopIteration
        value = self.cached
        self.cached = None
        self.ready = False
        return value

    def hasNext(self) -> bool:
        if self.ready:
            return True

        while self.stack:
            try:
                value = next(self.stack[-1])
            except StopIteration:
                self.stack.pop()
                continue

            if value.isInteger():
                self.cached = value.getInteger()
                self.ready = True
                return True
            self.stack.append(iter(value.getList()))

        return False


def solve(nestedList: list[NestedInteger]) -> list[int]:
    iterator = NestedIterator(nestedList)
    flattened = []
    while iterator.hasNext():
        flattened.append(iterator.next())
    return flattened
