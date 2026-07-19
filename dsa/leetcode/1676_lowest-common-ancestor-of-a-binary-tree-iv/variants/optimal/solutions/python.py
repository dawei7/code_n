def solve(root, nodes):
    targets = set(nodes)

    def search(node):
        if node is None or node in targets:
            return node

        left = search(node.left)
        right = search(node.right)
        if left is not None and right is not None:
            return node
        return left if left is not None else right

    return search(root)
