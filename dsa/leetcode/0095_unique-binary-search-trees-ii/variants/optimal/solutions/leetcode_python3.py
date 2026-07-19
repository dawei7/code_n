from functools import cache
from typing import List, Optional


class Solution:
    def generateTrees(self, n: int) -> List[Optional["TreeNode"]]:
        @cache
        def build(left: int, right: int):
            if left > right:
                return (None,)

            trees = []
            for root_value in range(left, right + 1):
                for left_tree in build(left, root_value - 1):
                    for right_tree in build(root_value + 1, right):
                        trees.append(TreeNode(root_value, left_tree, right_tree))
            return tuple(trees)

        return list(build(1, n))
