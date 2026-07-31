from typing import Any


class ListNode:
    """Local equivalent of LeetCode's ListNode for the standalone app template."""

    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


class TreeNode:
    """Local equivalent of the binary-tree node supplied by LeetCode's judge."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solve(head: Any | None):
    size = 0
    node = head
    while node is not None:
        size += 1
        node = node.next

    cursor = head

    def build(count: int):
        nonlocal cursor
        if count == 0:
            return None
        left = build(count // 2)
        root = TreeNode(cursor.val)
        cursor = cursor.next
        root.left = left
        root.right = build(count - count // 2 - 1)
        return root

    return build(size)
