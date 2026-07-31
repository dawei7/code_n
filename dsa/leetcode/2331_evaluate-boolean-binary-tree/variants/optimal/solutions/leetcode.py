from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root.left is None:
            return bool(root.val)

        left_value = self.evaluateTree(root.left)
        right_value = self.evaluateTree(root.right)
        if root.val == 2:
            return left_value or right_value
        return left_value and right_value
