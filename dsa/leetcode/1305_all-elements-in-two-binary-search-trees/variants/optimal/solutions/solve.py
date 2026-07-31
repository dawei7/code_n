"""Optimal app-local solution for LeetCode 1305."""


class TreeNode:
    """Local equivalent of LeetCode's TreeNode for the standalone app template."""

    def __init__(
        self,
        val: int = 0,
        left: "TreeNode | None" = None,
        right: "TreeNode | None" = None,
    ):
        self.val = val
        self.left = left
        self.right = right


def solve(root1, root2):
    def inorder(root):
        values = []
        stack = []
        node = root

        while node is not None or stack:
            while node is not None:
                stack.append(node)
                node = node.left
            node = stack.pop()
            values.append(node.val)
            node = node.right

        return values

    first = inorder(root1)
    second = inorder(root2)
    merged = []
    i = j = 0

    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            merged.append(first[i])
            i += 1
        else:
            merged.append(second[j])
            j += 1

    merged.extend(first[i:])
    merged.extend(second[j:])
    return merged
