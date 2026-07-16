from typing import Optional


class BSTIterator:
    def __init__(self, root: Optional["TreeNode"]):
        self.stack = []
        self.values = []
        self.index = -1
        self._push_left(root)

    def _push_left(self, node: Optional["TreeNode"]) -> None:
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
