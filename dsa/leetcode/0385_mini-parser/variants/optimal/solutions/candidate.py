"""Proposed app-local solution for LeetCode 385."""


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


def solve(s: str) -> NestedInteger:
    if s[0] != "[":
        return NestedInteger(int(s))

    root = NestedInteger()
    stack = [root]
    number_start = None

    for i, character in enumerate(s):
        if character == "[":
            if i > 0:
                nested = NestedInteger()
                stack[-1].add(nested)
                stack.append(nested)
        elif character == "," or character == "]":
            if number_start is not None:
                stack[-1].add(NestedInteger(int(s[number_start:i])))
                number_start = None
            if character == "]" and len(stack) > 1:
                stack.pop()
        elif number_start is None:
            number_start = i

    return root
