from functools import cache


class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right


def solve(n: int) -> list[TreeNode]:
    @cache
    def build(left: int, right: int) -> tuple[TreeNode | None, ...]:
        if left > right:
            return (None,)

        trees: list[TreeNode] = []
        for root_value in range(left, right + 1):
            for left_tree in build(left, root_value - 1):
                for right_tree in build(root_value + 1, right):
                    trees.append(TreeNode(root_value, left_tree, right_tree))
        return tuple(trees)

    return list(build(1, n))
