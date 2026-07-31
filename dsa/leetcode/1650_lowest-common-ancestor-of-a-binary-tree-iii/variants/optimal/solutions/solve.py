class Node:
    """Local equivalent of LeetCode's Node for the standalone app template."""

    def __init__(
        self,
        val: int = 0,
        left: "Node | None" = None,
        right: "Node | None" = None,
        parent: "Node | None" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


def solve(p: Node, q: Node) -> Node:
    first, second = p, q
    while first is not second:
        first = first.parent if first is not None else q
        second = second.parent if second is not None else p
    return first
