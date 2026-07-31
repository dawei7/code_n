from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        total = 0
        stack = [(root, None, None)]

        while stack:
            node, parent_value, grandparent_value = stack.pop()
            if grandparent_value is not None and grandparent_value % 2 == 0:
                total += node.val

            if node.left is not None:
                stack.append((node.left, node.val, parent_value))
            if node.right is not None:
                stack.append((node.right, node.val, parent_value))

        return total
