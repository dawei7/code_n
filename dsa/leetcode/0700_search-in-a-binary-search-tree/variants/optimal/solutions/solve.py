def solve(root, val: int):
    current = root

    while current is not None:
        if current.val == val:
            return current
        if val < current.val:
            current = current.left
        else:
            current = current.right

    return None
