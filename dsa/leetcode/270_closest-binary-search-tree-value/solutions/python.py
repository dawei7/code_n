def solve(root, target: float) -> int:
    closest = root.val
    node = root
    while node is not None:
        if (abs(node.val - target), node.val) < (abs(closest - target), closest):
            closest = node.val
        if node.val == target:
            return node.val
        node = node.left if target < node.val else node.right
    return closest
