from typing import Optional


class Solution:
    def longestConsecutive(self, root: Optional["TreeNode"]) -> int:
        if root is None:
            return 0
        best = 0
        stack = [(root, None, 0)]
        while stack:
            node, parent_value, parent_length = stack.pop()
            length = (
                parent_length + 1
                if parent_value is not None and node.val == parent_value + 1
                else 1
            )
            best = max(best, length)
            if node.right is not None:
                stack.append((node.right, node.val, length))
            if node.left is not None:
                stack.append((node.left, node.val, length))
        return best
