from collections import deque
from typing import Optional


class Solution:
    def isEvenOddTree(self, root: Optional['TreeNode']) -> bool:
        queue = deque([root])
        even_level = True

        while queue:
            previous = 0 if even_level else float("inf")
            for _ in range(len(queue)):
                node = queue.popleft()
                if even_level:
                    if node.val % 2 == 0 or node.val <= previous:
                        return False
                elif node.val % 2 == 1 or node.val >= previous:
                    return False

                previous = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            even_level = not even_level

        return True
