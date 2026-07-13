def solve(root, p: int, q: int) -> int:
    def search(node):
        if node is None or node.val == p or node.val == q:
            return node
        left = search(node.left)
        right = search(node.right)
        if left is not None and right is not None:
            return node
        return left if left is not None else right

    ancestor = search(root)
    if ancestor is None:
        raise ValueError("targets are not present in the tree")
    return ancestor.val
