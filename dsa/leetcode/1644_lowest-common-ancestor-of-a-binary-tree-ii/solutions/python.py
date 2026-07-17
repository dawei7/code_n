def solve(root, p: int, q: int) -> int | None:
    def search(node):
        if node is None:
            return None, 0

        left_candidate, left_found = search(node.left)
        right_candidate, right_found = search(node.right)
        found = left_found + right_found + (node.val == p) + (node.val == q)

        if left_candidate is not None and right_candidate is not None:
            candidate = node
        elif node.val == p or node.val == q:
            candidate = node
        else:
            candidate = left_candidate or right_candidate
        return candidate, found

    candidate, found = search(root)
    return candidate.val if found == 2 else None
