"""Single-pass stack parser for LeetCode 536."""

from __future__ import annotations


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: "TreeNode | None" = None,
        right: "TreeNode | None" = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


def solve(s: str) -> TreeNode | None:
    if not s:
        return None

    stack: list[list[TreeNode | int]] = []
    root: TreeNode | None = None
    cursor = 0
    while cursor < len(s):
        character = s[cursor]
        if character == "(":
            if cursor + 1 < len(s) and s[cursor + 1] == ")":
                stack[-1][1] = int(stack[-1][1]) + 1
                cursor += 2
            else:
                cursor += 1
            continue
        if character == ")":
            stack.pop()
            cursor += 1
            continue

        start = cursor
        if s[cursor] == "-":
            cursor += 1
        while cursor < len(s) and s[cursor].isdigit():
            cursor += 1
        node = TreeNode(int(s[start:cursor]))
        if stack:
            parent = stack[-1][0]
            slot = int(stack[-1][1])
            if slot == 0:
                parent.left = node  # type: ignore[union-attr]
            else:
                parent.right = node  # type: ignore[union-attr]
            stack[-1][1] = slot + 1
        else:
            root = node
        stack.append([node, 0])

    return root
