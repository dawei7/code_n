def solve(root):
    good = 0
    stack = [(root, root.val)]

    while stack:
        node, path_maximum = stack.pop()
        if node.val >= path_maximum:
            good += 1

        next_maximum = max(path_maximum, node.val)
        if node.left is not None:
            stack.append((node.left, next_maximum))
        if node.right is not None:
            stack.append((node.right, next_maximum))

    return good
