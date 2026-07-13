from typing import Optional


class Solution:
    def flatten(self, root: Optional["TreeNode"]) -> None:
        current = root
        while current is not None:
            if current.left is not None:
                predecessor = current.left
                while predecessor.right is not None:
                    predecessor = predecessor.right
                predecessor.right = current.right
                current.right = current.left
                current.left = None
            current = current.right
