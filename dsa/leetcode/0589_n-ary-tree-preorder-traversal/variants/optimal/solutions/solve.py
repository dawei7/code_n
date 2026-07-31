class Node:
    """Local equivalent of LeetCode's Node for the standalone app template."""

    def __init__(self, val: int = 0, children: "list[Node] | None" = None):
        self.val = val
        self.children = [] if children is None else children


def solve(root: Node | None) -> list[int]:
    if root is None:
        return []

    traversal: list[int] = []
    stack = [root]
    while stack:
        node = stack.pop()
        traversal.append(node.val)
        stack.extend(reversed(node.children))

    return traversal
