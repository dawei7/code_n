from typing import Any


def solve(root: Any) -> bool:
    if root.left is None:
        return bool(root.val)

    left_value = solve(root.left)
    right_value = solve(root.right)
    if root.val == 2:
        return left_value or right_value
    return left_value and right_value
