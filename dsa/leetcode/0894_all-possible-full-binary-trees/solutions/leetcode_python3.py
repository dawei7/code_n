from functools import cache
from typing import List, Optional


class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional["TreeNode"]]:
        @cache
        def build_shapes(nodes: int) -> tuple[tuple, ...]:
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

        def materialize(shape: tuple) -> "TreeNode":
            left_shape, right_shape = shape
            left = materialize(left_shape) if left_shape is not None else None
            right = materialize(right_shape) if right_shape is not None else None
            return TreeNode(0, left, right)

        return [materialize(shape) for shape in build_shapes(n)]
