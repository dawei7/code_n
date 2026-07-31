"""Optimal app-local solution for LeetCode 430."""


class Node:
    """Local equivalent of LeetCode's multilevel doubly linked-list node."""

    def __init__(
        self,
        val: int = 0,
        prev: "Node | None" = None,
        next: "Node | None" = None,
        child: "Node | None" = None,
    ):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


def solve(head: Node | None) -> Node | None:
    if head is None:
        return None

    stack = [head]
    previous = None
    while stack:
        current = stack.pop()
        if current.next is not None:
            stack.append(current.next)
        if current.child is not None:
            stack.append(current.child)
        if previous is not None:
            previous.next = current
            current.prev = previous
        current.child = None
        previous = current
    return head
