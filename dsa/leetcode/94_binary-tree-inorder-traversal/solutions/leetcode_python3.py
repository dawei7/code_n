from typing import List, Optional


class Solution:
    def inorderTraversal(self, root: Optional["TreeNode"]) -> List[int]:
        result = []
        stack = []
        node = root

        while node is not None or stack:
            while node is not None:
                stack.append(node)
                node = node.left
            node = stack.pop()
            result.append(node.val)
            node = node.right

        return result
