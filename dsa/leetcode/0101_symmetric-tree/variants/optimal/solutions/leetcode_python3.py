from typing import Optional


class Solution:
    def isSymmetric(self, root: Optional["TreeNode"]) -> bool:
        def mirror(left, right):
            if left is None or right is None:
                return left is right
            return (
                left.val == right.val
                and mirror(left.left, right.right)
                and mirror(left.right, right.left)
            )

        return root is None or mirror(root.left, root.right)
