"""Optimal app-local solution for LeetCode 894."""

from __future__ import annotations

from functools import cache


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: "TreeNode | None" = None,
        right: "TreeNode | None" = None,
    ):
        self.val = val
        self.left = left
        self.right = right


def solve(n):
    @cache
    def build_shapes(nodes):
        if nodes == 1:
            return ((None, None),)
        if nodes % 2 == 0:
            return ()

        shapes = []
        for left_nodes in range(1, nodes, 2):
            right_nodes = nodes - 1 - left_nodes
            for left in build_shapes(left_nodes):
                for right in build_shapes(right_nodes):
                    shapes.append((left, right))
        return tuple(shapes)

    def materialize(shape):
        left_shape, right_shape = shape
        left = materialize(left_shape) if left_shape is not None else None
        right = materialize(right_shape) if right_shape is not None else None
        return TreeNode(0, left, right)

    return [materialize(shape) for shape in build_shapes(n)]
