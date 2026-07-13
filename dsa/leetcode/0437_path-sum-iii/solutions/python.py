"""Optimal app-local solution for LeetCode 437."""


def solve(root: list, targetSum: int) -> int:
    if not root:
        return 0

    nodes = [None if value is None else {"value": value, "left": None, "right": None} for value in root]
    child_index = 1
    for node in nodes:
        if node is None:
            continue
        if child_index < len(nodes):
            node["left"] = nodes[child_index]
            child_index += 1
        if child_index < len(nodes):
            node["right"] = nodes[child_index]
            child_index += 1

    prefix_counts = {0: 1}

    def count_paths(node, current_sum: int) -> int:
        if node is None:
            return 0
        current_sum += node["value"]
        total = prefix_counts.get(current_sum - targetSum, 0)
        prefix_counts[current_sum] = prefix_counts.get(current_sum, 0) + 1
        total += count_paths(node["left"], current_sum)
        total += count_paths(node["right"], current_sum)
        prefix_counts[current_sum] -= 1
        return total

    return count_paths(nodes[0], 0)
