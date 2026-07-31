"""Optimal app-local solution for LeetCode 3294."""


class Node:
    """Local equivalent of LeetCode's doubly linked-list node."""

    def __init__(
        self,
        val: int = 0,
        prev: "Node | None" = None,
        next: "Node | None" = None,
    ):
        self.val = val
        self.prev = prev
        self.next = next


def solve(node: Node | None) -> list[int]:
    while node is not None and node.prev is not None:
        node = node.prev

    values = []
    while node is not None:
        values.append(node.val)
        node = node.next
    return values
