from typing import Any


class BSTIterator:
    def __init__(self, root: Any | None):
        self.stack: list[Any] = []
        self.values: list[int] = []
        self.index = -1
        self._push_left(root)

    def _push_left(self, node: Any | None) -> None:
        while node is not None:
            self.stack.append(node)
            node = node.left

    def hasNext(self) -> bool:
        return self.index + 1 < len(self.values) or bool(self.stack)

    def next(self) -> int:
        self.index += 1
        if self.index == len(self.values):
            node = self.stack.pop()
            self.values.append(node.val)
            self._push_left(node.right)
        return self.values[self.index]

    def hasPrev(self) -> bool:
        return self.index > 0

    def prev(self) -> int:
        self.index -= 1
        return self.values[self.index]


def solve(root: Any | None, operations: list[str]) -> list[int | bool | None]:
    iterator: BSTIterator | None = None
    output: list[int | bool | None] = []
    for operation in operations:
        if operation == "BSTIterator":
            iterator = BSTIterator(root)
            output.append(None)
        elif operation == "next":
            assert iterator is not None
            output.append(iterator.next())
        elif operation == "hasNext":
            assert iterator is not None
            output.append(iterator.hasNext())
        elif operation == "prev":
            assert iterator is not None
            output.append(iterator.prev())
        elif operation == "hasPrev":
            assert iterator is not None
            output.append(iterator.hasPrev())
        else:
            raise ValueError(f"unknown operation: {operation}")
    return output
