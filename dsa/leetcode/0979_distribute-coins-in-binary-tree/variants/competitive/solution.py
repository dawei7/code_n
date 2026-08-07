from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        moves = 0

        def balance(node):
            nonlocal moves
            if node is None:
                return 0
            left = balance(node.left)
            right = balance(node.right)
            moves += abs(left) + abs(right)
            return node.val + left + right - 1

        balance(root)
        return moves
