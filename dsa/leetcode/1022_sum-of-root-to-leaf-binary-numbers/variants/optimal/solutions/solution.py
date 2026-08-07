from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def visit(node: Optional[TreeNode], prefix: int) -> int:
            if node is None:
                return 0

            current = prefix * 2 + node.val
            if node.left is None and node.right is None:
                return current

            return visit(node.left, current) + visit(node.right, current)

        return visit(root, 0)
