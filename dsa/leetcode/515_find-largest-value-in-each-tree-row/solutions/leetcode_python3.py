from collections import deque
from typing import List, Optional


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        answer = []
        queue = deque([root])
        while queue:
            row_maximum = queue[0].val
            for _ in range(len(queue)):
                node = queue.popleft()
                row_maximum = max(row_maximum, node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            answer.append(row_maximum)
        return answer
