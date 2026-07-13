from typing import List, Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional['TreeNode']) -> List[int]:
        if root is None:
            return []

        def is_leaf(node: 'TreeNode') -> bool:
            return node.left is None and node.right is None

        boundary = [root.val]

        node = root.left
        while node is not None:
            if not is_leaf(node):
                boundary.append(node.val)
            node = node.left if node.left is not None else node.right

        stack = [root]
        while stack:
            node = stack.pop()
            if is_leaf(node):
                if node is not root:
                    boundary.append(node.val)
                continue
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)

        right_boundary = []
        node = root.right
        while node is not None:
            if not is_leaf(node):
                right_boundary.append(node.val)
            node = node.right if node.right is not None else node.left

        boundary.extend(reversed(right_boundary))
        return boundary

