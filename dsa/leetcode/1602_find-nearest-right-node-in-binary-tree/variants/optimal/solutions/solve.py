from collections import deque


class TreeNode:
    """Local equivalent of LeetCode's TreeNode for the standalone app template."""

    def __init__(
        self,
        val: int = 0,
        left: "TreeNode | None" = None,
        right: "TreeNode | None" = None,
    ):
        self.val = val
        self.left = left
        self.right = right


def solve(root, u):
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
