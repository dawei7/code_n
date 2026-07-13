from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional['TreeNode']) -> int:
        stack = []
        node = root
        previous = None
        minimum = float("inf")

        while stack or node is not None:
            while node is not None:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if previous is not None:
                minimum = min(minimum, node.val - previous)
            previous = node.val
            node = node.right

        return int(minimum)
