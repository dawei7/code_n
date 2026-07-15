from collections import deque
from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.incomplete = deque()
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node.left is None or node.right is None:
                self.incomplete.append(node)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

    def insert(self, val: int) -> int:
        parent = self.incomplete[0]
        node = TreeNode(val)

        if parent.left is None:
            parent.left = node
        else:
            parent.right = node
            self.incomplete.popleft()

        self.incomplete.append(node)
        return parent.val

    def get_root(self) -> Optional[TreeNode]:
        return self.root

