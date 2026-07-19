from typing import Any


def solve(root: Any | None) -> bool:
    def mirror(left: Any | None, right: Any | None) -> bool:
        if left is None or right is None:
            return left is right
        return (
            left.val == right.val
            and mirror(left.left, right.right)
            and mirror(left.right, right.left)
        )

    return root is None or mirror(root.left, root.right)
