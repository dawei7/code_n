# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def correctBinaryTree(self, root: 'TreeNode') -> 'TreeNode':
        seen = set()

        def repair(node):
            if node is None:
                return None
            if node.right in seen:
                return None

            seen.add(node)
            node.right = repair(node.right)
            node.left = repair(node.left)
            return node

        return repair(root)
