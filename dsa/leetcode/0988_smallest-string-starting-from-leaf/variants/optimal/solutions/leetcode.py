from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        path = []
        best = None
        stack = [(root, False)]

        while stack:
            node, exiting = stack.pop()
            if exiting:
                path.pop()
                continue

            path.append(chr(ord("a") + node.val))
            stack.append((node, True))

            if node.left is None and node.right is None:
                candidate = "".join(reversed(path))
                if best is None or candidate < best:
                    best = candidate
            else:
                if node.right is not None:
                    stack.append((node.right, False))
                if node.left is not None:
                    stack.append((node.left, False))

        return best
