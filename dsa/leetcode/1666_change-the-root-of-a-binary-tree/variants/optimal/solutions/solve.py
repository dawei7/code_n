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


def solve(root: Node, leaf: Node) -> Node:
    current = leaf
    parent = current.parent

    while current is not root:
        grandparent = parent.parent
        if current.left is not None:
            current.right = current.left
        current.left = parent
        parent.parent = current

        if parent.left is current:
            parent.left = None
        else:
            parent.right = None

        current = parent
        parent = grandparent

    leaf.parent = None
    return leaf
