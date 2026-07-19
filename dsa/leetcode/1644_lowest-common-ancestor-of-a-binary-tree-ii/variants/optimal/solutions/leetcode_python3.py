# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'
    ) -> 'TreeNode':
        def search(node):
            if node is None:
                return None, 0

            left_candidate, left_found = search(node.left)
            right_candidate, right_found = search(node.right)
            found = left_found + right_found + (node is p) + (node is q)

            if left_candidate is not None and right_candidate is not None:
                candidate = node
            elif node is p or node is q:
                candidate = node
            else:
                candidate = left_candidate or right_candidate
            return candidate, found

        candidate, found = search(root)
        return candidate if found == 2 else None
