class Node:
    """Local equivalent of LeetCode's Node for the standalone app template."""

    def __init__(
        self,
        val: int = 0,
        left: "Node | None" = None,
        right: "Node | None" = None,
        next: "Node | None" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def solve(root: Node | None) -> Node | None:
    leftmost = root
    while leftmost is not None and leftmost.left is not None:
        node = leftmost
        while node is not None:
            node.left.next = node.right
            node.right.next = node.next.left if node.next is not None else None
            node = node.next
        leftmost = leftmost.left
    return root
