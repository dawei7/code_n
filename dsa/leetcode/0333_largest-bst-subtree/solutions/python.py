def _largest_bst_subtree(root) -> int:
    if root is None:
        return 0

    empty = (True, float("inf"), float("-inf"), 0, 0)
    summaries = {}
    stack = [(root, False)]
    while stack:
        node, expanded = stack.pop()
        if node is None:
            continue
        if not expanded:
            stack.append((node, True))
            stack.append((node.right, False))
            stack.append((node.left, False))
            continue

        left_valid, left_minimum, left_maximum, left_size, left_best = summaries.get(
            node.left, empty
        )
        right_valid, right_minimum, right_maximum, right_size, right_best = summaries.get(
            node.right, empty
        )
        if left_valid and right_valid and left_maximum < node.val < right_minimum:
            size = 1 + left_size + right_size
            summaries[node] = (
                True,
                min(left_minimum, node.val),
                max(right_maximum, node.val),
                size,
                size,
            )
        else:
            summaries[node] = (False, 0, 0, 0, max(left_best, right_best))

    return summaries[root][4]


def solve(root) -> int:
    return _largest_bst_subtree(root)
