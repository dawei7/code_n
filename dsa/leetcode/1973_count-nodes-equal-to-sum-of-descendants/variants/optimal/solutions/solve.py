from typing import Any


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


def solve(root: Any) -> int:
    stack = [(root, False)]
    subtree_sums: dict[Any, int] = {}
    answer = 0

    while stack:
        node, visited = stack.pop()
        if node is None:
            continue
        if not visited:
            stack.append((node, True))
            stack.append((node.right, False))
            stack.append((node.left, False))
            continue

        descendant_sum = subtree_sums.get(node.left, 0) + subtree_sums.get(node.right, 0)
        if node.val == descendant_sum:
            answer += 1
        subtree_sums[node] = node.val + descendant_sum

    return answer
