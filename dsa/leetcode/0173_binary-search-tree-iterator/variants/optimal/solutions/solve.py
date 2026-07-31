class TreeNode:
    """Local equivalent of the binary-tree node supplied by LeetCode's judge."""

    def __init__(
        self,
        val: int = 0,
        left: "TreeNode | None" = None,
        right: "TreeNode | None" = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: TreeNode | None):
        self.stack: list[TreeNode] = []
        self._push_left(root)

    def _push_left(self, node: TreeNode | None) -> None:
        while node is not None:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        node = self.stack.pop()
        self._push_left(node.right)
        return node.val

    def hasNext(self) -> bool:
        return bool(self.stack)


def solve(
    root: TreeNode | None,
    operations: list[str],
) -> list[int | bool | None]:
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
        else:
            raise ValueError(f"unknown operation: {operation}")
    return output
