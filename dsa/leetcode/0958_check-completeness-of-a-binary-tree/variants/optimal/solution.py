from collections import deque
from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        missing_seen = False

        while queue:
            node = queue.popleft()
            if node is None:
                missing_seen = True
                continue
            if missing_seen:
                return False
            queue.append(node.left)
            queue.append(node.right)
        return True
