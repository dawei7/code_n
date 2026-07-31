"""Parent-pointer inorder successor for LeetCode 510."""


class Node:
    """Local equivalent of LeetCode's Node for the standalone app template."""

    def __init__(
        self,
        val: int = 0,
        left: "Node | None" = None,
        right: "Node | None" = None,
        parent: "Node | None" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


def solve(node: Node) -> Node | None:
    if node.right is not None:
        successor = node.right
        while successor.left is not None:
            successor = successor.left
        return successor

    current = node
    while current.parent is not None and current is current.parent.right:
        current = current.parent
    return current.parent
