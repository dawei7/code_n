def solve(root, p: int):
    successor = None
    node = root
    while node is not None:
        if node.val > p:
            successor = node
            node = node.left
        else:
            node = node.right
    return successor.val if successor is not None else None
