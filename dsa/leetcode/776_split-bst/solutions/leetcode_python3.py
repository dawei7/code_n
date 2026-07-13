from typing import List, Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def splitBST(
        self, root: "Optional[TreeNode]", target: int
    ) -> "List[Optional[TreeNode]]":
        if root is None:
            return [None, None]
        if root.val <= target:
            smaller_right, greater = self.splitBST(root.right, target)
            root.right = smaller_right
            return [root, greater]

        smaller, greater_left = self.splitBST(root.left, target)
        root.left = greater_left
        return [smaller, root]
