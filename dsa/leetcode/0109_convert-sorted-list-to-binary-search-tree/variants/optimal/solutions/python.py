from typing import Any


class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right


def solve(head: Any | None) -> TreeNode | None:
    size = 0
    node = head
    while node is not None:
        size += 1
        node = node.next

    cursor = head

    def build(count: int) -> TreeNode | None:
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
