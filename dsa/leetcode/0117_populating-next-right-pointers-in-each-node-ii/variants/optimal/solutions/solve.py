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
    current_level = root
    while current_level is not None:
        next_head = tail = None
        node = current_level
        while node is not None:
            for child in (node.left, node.right):
                if child is None:
                    continue
                if tail is None:
                    next_head = child
                else:
                    tail.next = child
                tail = child
            node = node.next
        if tail is not None:
            tail.next = None
        current_level = next_head
    return root
