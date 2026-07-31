from collections import defaultdict


class Node:
    """Local equivalent of LeetCode's Node for the standalone app template."""

    def __init__(
        self,
        val: str = "",
        left: "Node | None" = None,
        right: "Node | None" = None,
    ):
        self.val = val
        self.left = left
        self.right = right


def solve(root1: Node, root2: Node) -> bool:
    balance: dict[str, int] = defaultdict(int)

    def collect(node: Node, delta: int) -> None:
        if node.val == "+":
            collect(node.left, delta)
            collect(node.right, delta)
        else:
            balance[node.val] += delta

    collect(root1, 1)
    collect(root2, -1)
    return all(count == 0 for count in balance.values())
