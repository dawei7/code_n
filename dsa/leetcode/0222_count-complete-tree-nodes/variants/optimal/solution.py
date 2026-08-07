from typing import Optional


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def left_height(node):
            height = 0
            while node:
                height += 1
                node = node.left
            return height

        if not root:
            return 0
        left = left_height(root.left)
        right = left_height(root.right)
        if left == right:
            return (1 << left) + self.countNodes(root.right)
        return (1 << right) + self.countNodes(root.left)
