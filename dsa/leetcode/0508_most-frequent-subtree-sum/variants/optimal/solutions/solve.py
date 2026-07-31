"""Iterative postorder subtree aggregation for LeetCode 508."""

from collections import Counter


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
    subtree_sum = {}
    frequencies = Counter()
    maximum_frequency = 0
    stack = [(root, False)]

    while stack:
        node, expanded = stack.pop()
        if node is None:
            continue
        if not expanded:
            stack.append((node, True))
            stack.append((node.right, False))
            stack.append((node.left, False))
            continue

        total = node.val + subtree_sum.get(node.left, 0) + subtree_sum.get(node.right, 0)
        subtree_sum[node] = total
        frequencies[total] += 1
        maximum_frequency = max(maximum_frequency, frequencies[total])

    return [total for total, count in frequencies.items() if count == maximum_frequency]
