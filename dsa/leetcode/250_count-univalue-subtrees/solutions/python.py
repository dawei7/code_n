def solve(root) -> int:
    count = 0

    def is_univalue(node) -> bool:
        nonlocal count
        if node is None:
            return True
        left_ok = is_univalue(node.left)
        right_ok = is_univalue(node.right)
        if not left_ok or not right_ok:
            return False
        if node.left is not None and node.left.val != node.val:
            return False
        if node.right is not None and node.right.val != node.val:
            return False
        count += 1
        return True

    is_univalue(root)
    return count
