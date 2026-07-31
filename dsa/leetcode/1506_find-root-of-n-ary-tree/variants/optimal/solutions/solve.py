"""Optimal app-local solution for LeetCode 1506."""


class Node:
    """Local equivalent of LeetCode's N-ary tree node."""

    def __init__(self, val: int = 0, children: "list[Node] | None" = None):
        self.val = val
        self.children = [] if children is None else children


def solve(tree: list[Node]) -> Node:
    root_value = 0
    for node in tree:
        root_value ^= node.val
        for child in node.children:
            root_value ^= child.val

    for node in tree:
        if node.val == root_value:
            return node
