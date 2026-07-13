"""Iterative preorder codec for LeetCode 297."""

from typing import Any


class _Node:
    def __init__(self, value: int):
        self.val = value
        self.left: Any | None = None
        self.right: Any | None = None


def _serialize(root: Any | None) -> str:
    tokens: list[str] = []
    stack = [root]
    while stack:
        node = stack.pop()
        if node is None:
            tokens.append("#")
            continue
        tokens.append(str(node.val))
        stack.append(node.right)
        stack.append(node.left)
    return ",".join(tokens)


def _deserialize(data: str) -> _Node | None:
    tokens = data.split(",")
    if tokens[0] == "#":
        return None
    root = _Node(int(tokens[0]))
    stack: list[tuple[_Node, int]] = [(root, 0)]
    for token in tokens[1:]:
        child = None if token == "#" else _Node(int(token))
        parent, slot = stack[-1]
        if slot == 0:
            parent.left = child
            stack[-1] = (parent, 1)
        else:
            parent.right = child
            stack.pop()
        if child is not None:
            stack.append((child, 0))
    return root


def solve(root: Any | None) -> _Node | None:
    return _deserialize(_serialize(root))
