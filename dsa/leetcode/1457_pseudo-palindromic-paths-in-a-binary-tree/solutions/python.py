def solve(root):
    total = 0
    stack = [(root, 0)]

    while stack:
        node, mask = stack.pop()
        mask ^= 1 << node.val

        if node.left is None and node.right is None:
            if mask & (mask - 1) == 0:
                total += 1
            continue

        if node.left is not None:
            stack.append((node.left, mask))
        if node.right is not None:
            stack.append((node.right, mask))

    return total
