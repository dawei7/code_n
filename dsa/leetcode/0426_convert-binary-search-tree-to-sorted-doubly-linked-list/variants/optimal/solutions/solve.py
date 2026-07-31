"""Optimal app-local solution for LeetCode 426."""


class Node:
    """Local equivalent of LeetCode's Node for the standalone app template."""

    def __init__(
        self,
        val: int = 0,
        left: "Node | None" = None,
        right: "Node | None" = None,
    ):
        self.val = val
        self.left = left
        self.right = right


def solve(root: Node | None) -> Node | None:
    if root is None:
        return None

    first = None
    previous = None

    def inorder(node: Node | None) -> None:
        nonlocal first, previous
        if node is None:
            return

        inorder(node.left)
        if previous is None:
            first = node
        else:
            previous.right = node
            node.left = previous
        previous = node
        inorder(node.right)

    inorder(root)
    first.left = previous
    previous.right = first
    return first
