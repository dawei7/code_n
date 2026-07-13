from typing import Any


def solve(root: Any) -> int:
    best = float("-inf")

    def gain(node: Any | None) -> int:
        nonlocal best
        if node is None:
            return 0
        left_gain = max(0, gain(node.left))
        right_gain = max(0, gain(node.right))
        best = max(best, node.val + left_gain + right_gain)
        return node.val + max(left_gain, right_gain)

    gain(root)
    return int(best)
