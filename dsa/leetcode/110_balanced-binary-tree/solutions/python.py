from typing import Any


def solve(root: Any | None) -> bool:
    def height(node: Any | None) -> int:
        if node is None:
            return 0
        left_height = height(node.left)
        if left_height < 0:
            return -1
        right_height = height(node.right)
        if right_height < 0 or abs(left_height - right_height) > 1:
            return -1
        return 1 + max(left_height, right_height)

    return height(root) >= 0
