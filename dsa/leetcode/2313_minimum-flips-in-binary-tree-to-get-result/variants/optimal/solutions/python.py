from typing import Any


def solve(root: Any, result: bool) -> int:
    costs: dict[Any, tuple[int, int]] = {}
    stack = [(root, False)]

    while stack:
        node, visited = stack.pop()
        if not visited:
            stack.append((node, True))
            if node.left:
                stack.append((node.left, False))
            if node.right:
                stack.append((node.right, False))
            continue

        if not node.left and not node.right:
            costs[node] = (0, 1) if node.val == 0 else (1, 0)
        elif node.val == 5:
            child = node.left or node.right
            false_cost, true_cost = costs[child]
            costs[node] = (true_cost, false_cost)
        else:
            left_costs = costs[node.left]
            right_costs = costs[node.right]
            best = [10**9, 10**9]
            for left_value in (0, 1):
                for right_value in (0, 1):
                    if node.val == 2:
                        value = left_value | right_value
                    elif node.val == 3:
                        value = left_value & right_value
                    else:
                        value = left_value ^ right_value
                    best[value] = min(
                        best[value],
                        left_costs[left_value] + right_costs[right_value],
                    )
            costs[node] = (best[0], best[1])

    return costs[root][result]
