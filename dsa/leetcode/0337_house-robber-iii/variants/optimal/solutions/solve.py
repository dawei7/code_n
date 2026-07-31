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


def solve(root: TreeNode | None) -> int:
    if root is None:
        return 0
    states = {}
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
        left_skip, left_take = states.get(node.left, (0, 0))
        right_skip, right_take = states.get(node.right, (0, 0))
        take = node.val + left_skip + right_skip
        skip = max(left_skip, left_take) + max(right_skip, right_take)
        states[node] = (skip, take)
    return max(states[root])
