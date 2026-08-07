from typing import Optional


class Solution:
    def increasingBST(self, root: Optional["TreeNode"]) -> Optional["TreeNode"]:
        dummy = TreeNode()
        tail = dummy
        stack = []
        current = root

        while stack or current is not None:
            while current is not None:
                stack.append(current)
                current = current.left

            current = stack.pop()
            original_right = current.right
            current.left = None
            tail.right = current
            tail = current
            current = original_right

        tail.right = None
        return dummy.right
