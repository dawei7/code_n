from typing import Optional


class Solution:
    def upsideDownBinaryTree(self, root: Optional["TreeNode"]) -> Optional["TreeNode"]:
        current = root
        parent = None
        parent_right = None
        while current is not None:
            following = current.left
            current.left = parent_right
            parent_right = current.right
            current.right = parent
            parent = current
            current = following
        return parent
