from typing import Any


def solve(root: Any | None, targetSum: int) -> bool:
    if root is None:
        return False
    stack = [(root, root.val)]
    while stack:
        node, path_sum = stack.pop()
        if node.left is None and node.right is None and path_sum == targetSum:
            return True
        if node.right is not None:
            stack.append((node.right, path_sum + node.right.val))
        if node.left is not None:
            stack.append((node.left, path_sum + node.left.val))
    return False
