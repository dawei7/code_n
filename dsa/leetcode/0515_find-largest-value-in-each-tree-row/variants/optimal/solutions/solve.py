"""Row-bounded breadth-first traversal for LeetCode 515."""

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


def solve(root) -> list[int]:
    if root is None:
        return []

    answer: list[int] = []
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
