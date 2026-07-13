from typing import List, Optional


class Solution:
    def postorderTraversal(self, root: Optional["TreeNode"]) -> List[int]:
        result = []
        stack = []
        current = root
        last_visited = None

        while current is not None or stack:
            if current is not None:
                stack.append(current)
                current = current.left
                continue

            node = stack[-1]
            if node.right is not None and last_visited is not node.right:
                current = node.right
            else:
                result.append(node.val)
                last_visited = stack.pop()
        return result
