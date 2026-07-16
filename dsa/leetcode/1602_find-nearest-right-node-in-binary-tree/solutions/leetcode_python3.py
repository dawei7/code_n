from collections import deque
from typing import Optional


class Solution:
    def findNearestRightNode(
        self,
        root: 'TreeNode',
        u: 'TreeNode',
    ) -> Optional['TreeNode']:
        queue = deque([root])
        while queue:
            level_size = len(queue)
            for index in range(level_size):
                node = queue.popleft()
                if node is u:
                    return queue[0] if index + 1 < level_size else None
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return None
