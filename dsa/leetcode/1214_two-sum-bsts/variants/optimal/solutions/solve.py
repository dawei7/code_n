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


def solve(root1, root2, target: int) -> bool:
    first_values = set()
    stack = [root1]
    while stack:
        node = stack.pop()
        if node is None:
            continue
        first_values.add(node.val)
        stack.append(node.left)
        stack.append(node.right)

    stack = [root2]
    while stack:
        node = stack.pop()
        if node is None:
            continue
        if target - node.val in first_values:
            return True
        stack.append(node.left)
        stack.append(node.right)
    return False
