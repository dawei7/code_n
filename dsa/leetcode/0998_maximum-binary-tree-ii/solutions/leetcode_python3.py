from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(
        self, root: Optional[TreeNode], val: int
    ) -> Optional[TreeNode]:
        inserted = TreeNode(val)

        if val > root.val:
            inserted.left = root
            return inserted

        current = root
        while current.right is not None and current.right.val > val:
            current = current.right

        inserted.left = current.right
        current.right = inserted
        return root
