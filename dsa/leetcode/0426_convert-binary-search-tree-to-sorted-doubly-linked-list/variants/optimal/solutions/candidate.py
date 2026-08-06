"""Inert review candidate for LeetCode 426."""


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

    first: Node | None = None
    previous: Node | None = None
    stack: list[Node] = []
    current: Node | None = root

    while stack or current is not None:
        while current is not None:
            stack.append(current)
            current = current.left

        current = stack.pop()
        right_subtree = current.right
        if previous is None:
            first = current
        else:
            previous.right = current
            current.left = previous
        previous = current
        current = right_subtree

    assert first is not None and previous is not None
    first.left = previous
    previous.right = first
    return first
