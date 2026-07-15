from typing import Optional


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        answer = 0
        stack = [(root, root.val, root.val)]

        while stack:
            node, path_min, path_max = stack.pop()
            answer = max(answer, node.val - path_min, path_max - node.val)
            next_min = min(path_min, node.val)
            next_max = max(path_max, node.val)
            if node.left is not None:
                stack.append((node.left, next_min, next_max))
            if node.right is not None:
                stack.append((node.right, next_min, next_max))

        return answer

