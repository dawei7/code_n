from itertools import zip_longest


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


def solve(root1, root2):
    def leaf_values(root):
        stack = [root] if root is not None else []
        while stack:
            node = stack.pop()
            if node.left is None and node.right is None:
                yield node.val
                continue
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)

    missing = object()
    return all(
        first == second
        for first, second in zip_longest(
            leaf_values(root1),
            leaf_values(root2),
            fillvalue=missing,
        )
    )
