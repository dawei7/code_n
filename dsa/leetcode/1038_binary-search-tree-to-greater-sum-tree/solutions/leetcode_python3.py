from typing import Optional


class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        running_sum = 0
        stack = []
        node = root

        while node is not None or stack:
            while node is not None:
                stack.append(node)
                node = node.right
            node = stack.pop()
            running_sum += node.val
            node.val = running_sum
            node = node.left

        return root

