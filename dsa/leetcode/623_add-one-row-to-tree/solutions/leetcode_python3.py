from collections import deque
from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def addOneRow(
        self,
        root: Optional[TreeNode],
        val: int,
        depth: int,
    ) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, left=root)

        level = 1
        queue = deque([root])
        while level < depth - 1:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            level += 1

        for node in queue:
            old_left = node.left
            old_right = node.right
            node.left = TreeNode(val, left=old_left)
            node.right = TreeNode(val, right=old_right)
        return root
