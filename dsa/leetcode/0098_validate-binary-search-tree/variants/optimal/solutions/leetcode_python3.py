from typing import Optional


class Solution:
    def isValidBST(self, root: Optional["TreeNode"]) -> bool:
        stack = [(root, float("-inf"), float("inf"))]

        while stack:
            node, lower, upper = stack.pop()
            if node is None:
                continue
            if not lower < node.val < upper:
                return False
            stack.append((node.right, node.val, upper))
            stack.append((node.left, lower, node.val))

        return True
