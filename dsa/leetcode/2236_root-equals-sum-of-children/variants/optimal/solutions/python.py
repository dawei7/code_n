def solve(root) -> bool:
    return root.val == root.left.val + root.right.val
