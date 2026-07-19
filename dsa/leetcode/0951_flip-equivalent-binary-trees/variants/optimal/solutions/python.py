"""Optimal app-local solution for LeetCode 951."""


def solve(root1, root2):
    if root1 is root2:
        return True
    if root1 is None or root2 is None or root1.val != root2.val:
        return False
    return (
        solve(root1.left, root2.left) and solve(root1.right, root2.right)
    ) or (
        solve(root1.left, root2.right) and solve(root1.right, root2.left)
    )
