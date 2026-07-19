"""Optimal app-local solution for LeetCode 979."""


def solve(root):
    moves = 0

    def balance(node):
        nonlocal moves
        if node is None:
            return 0
        left = balance(node.left)
        right = balance(node.right)
        moves += abs(left) + abs(right)
        return node.val + left + right - 1

    balance(root)
    return moves
