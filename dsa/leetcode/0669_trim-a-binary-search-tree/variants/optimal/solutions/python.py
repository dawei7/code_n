def solve(root, low: int, high: int):
    if root is None:
        return None
    if root.val < low:
        return solve(root.right, low, high)
    if root.val > high:
        return solve(root.left, low, high)

    root.left = solve(root.left, low, high)
    root.right = solve(root.right, low, high)
    return root

