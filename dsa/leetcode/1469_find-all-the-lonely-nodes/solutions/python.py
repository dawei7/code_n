def solve(root):
    lonely = []
    stack = [root]

    while stack:
        node = stack.pop()
        if node.left is None and node.right is not None:
            lonely.append(node.right.val)
        elif node.right is None and node.left is not None:
            lonely.append(node.left.val)

        if node.left is not None:
            stack.append(node.left)
        if node.right is not None:
            stack.append(node.right)

    return lonely
