def solve(root, leaf):
    current = leaf
    parent = current.parent

    while current is not root:
        grandparent = parent.parent
        if current.left is not None:
            current.right = current.left
        current.left = parent
        parent.parent = current

        if parent.left is current:
            parent.left = None
        else:
            parent.right = None

        current = parent
        parent = grandparent

    leaf.parent = None
    return leaf
