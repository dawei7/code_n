from typing import Any


def solve(root: Any) -> int:
    answer = 0
    summaries: dict[Any, tuple[int, int]] = {}
    stack = [(root, False)]

    while stack:
        node, processed = stack.pop()
        if not processed:
            stack.append((node, True))
            if node.right is not None:
                stack.append((node.right, False))
            if node.left is not None:
                stack.append((node.left, False))
            continue

        left_sum, left_count = summaries.get(node.left, (0, 0))
        right_sum, right_count = summaries.get(node.right, (0, 0))
        subtree_sum = left_sum + right_sum + node.val
        subtree_count = left_count + right_count + 1
        if subtree_sum // subtree_count == node.val:
            answer += 1
        summaries[node] = (subtree_sum, subtree_count)

    return answer
