from collections import deque
from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def mergeTrees(
        self,
        root1: Optional[TreeNode],
        root2: Optional[TreeNode],
    ) -> Optional[TreeNode]:
        if root1 is None and root2 is None:
            return None

        result = TreeNode(
            (root1.val if root1 is not None else 0)
            + (root2.val if root2 is not None else 0)
        )
        queue = deque([(result, root1, root2)])

        while queue:
            target, first, second = queue.popleft()
            for side in ("left", "right"):
                first_child = getattr(first, side) if first is not None else None
                second_child = getattr(second, side) if second is not None else None
                if first_child is None and second_child is None:
                    continue

                child = TreeNode(
                    (first_child.val if first_child is not None else 0)
                    + (second_child.val if second_child is not None else 0)
                )
                setattr(target, side, child)
                queue.append((child, first_child, second_child))

        return result
