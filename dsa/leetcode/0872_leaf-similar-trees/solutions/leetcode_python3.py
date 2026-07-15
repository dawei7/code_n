from itertools import zip_longest
from typing import Iterator, Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> bool:
        def leaf_values(root: Optional[TreeNode]) -> Iterator[int]:
            stack = [root] if root is not None else []
            while stack:
                node = stack.pop()
                if node.left is None and node.right is None:
                    yield node.val
                    continue
                if node.right is not None:
                    stack.append(node.right)
                if node.left is not None:
                    stack.append(node.left)

        missing = object()
        return all(
            first == second
            for first, second in zip_longest(
                leaf_values(root1),
                leaf_values(root2),
                fillvalue=missing,
            )
        )
