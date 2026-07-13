def solve(root, p: int, q: int) -> int:
    low, high = sorted((p, q))
    current = root
    while current is not None:
        if current.val < low:
            current = current.right
        elif current.val > high:
            current = current.left
        else:
            return current.val
    raise ValueError("targets are not present in the tree")
