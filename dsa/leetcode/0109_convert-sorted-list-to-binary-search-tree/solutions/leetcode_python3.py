from typing import Optional


class Solution:
    def sortedListToBST(self, head: Optional["ListNode"]) -> Optional["TreeNode"]:
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
