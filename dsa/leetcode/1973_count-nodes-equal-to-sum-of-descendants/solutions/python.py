from typing import Any


def solve(root: Any) -> int:
    stack = [(root, False)]
    subtree_sums: dict[Any, int] = {}
    answer = 0

    while stack:
        node, visited = stack.pop()
        if node is None:
            continue
        if not visited:
            stack.append((node, True))
            stack.append((node.right, False))
            stack.append((node.left, False))
            continue

        descendant_sum = subtree_sums.get(node.left, 0) + subtree_sums.get(node.right, 0)
        if node.val == descendant_sum:
            answer += 1
        subtree_sums[node] = node.val + descendant_sum

    return answer
