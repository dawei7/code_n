"""Optimal app-local solution for LeetCode 1008."""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solve(preorder):
    root = TreeNode(preorder[0])
    stack = [root]

    for value in preorder[1:]:
        node = TreeNode(value)
        if value < stack[-1].val:
            stack[-1].left = node
        else:
            parent = None
            while stack and stack[-1].val < value:
                parent = stack.pop()
            parent.right = node
        stack.append(node)

    return root
