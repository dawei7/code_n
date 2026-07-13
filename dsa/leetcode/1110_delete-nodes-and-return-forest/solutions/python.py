"""Optimal solution for LeetCode 1110: Delete Nodes And Return Forest."""

from __future__ import annotations

from typing import Any


def solve(root: Any | None, to_delete: list[int]) -> list[Any]:
    deleted = set(to_delete)
    forest: list[Any] = []

    def dfs(node: Any | None, is_root: bool) -> Any | None:
        if node is None:
            return None
        remove = node.val in deleted
        if is_root and not remove:
            forest.append(node)
        node.left = dfs(node.left, remove)
        node.right = dfs(node.right, remove)
        return None if remove else node

    dfs(root, True)
    return forest
