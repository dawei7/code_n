from typing import List

def solve(n: int, cost: List[int]) -> int:
    """
    Calculates the minimum total cost to make all root-to-leaf paths equal
    in a complete binary tree represented by an array.

    Args:
        n: The number of nodes in the complete binary tree.
        cost: A list of integers where cost[i] is the value of the i-th node.

    Returns:
        The minimum total cost added.
    """
    total_added_cost = 0

    # Iterate from the last parent node up to the root.
    # The last parent node in a 0-indexed complete binary tree is at index (n // 2) - 1.
    # The root node is at index 0.
    # We iterate downwards because we need to process children's subtrees
    # before their parents (bottom-up dynamic programming).
    for i in range(n // 2 - 1, -1, -1):
        left_child_idx = 2 * i + 1
        right_child_idx = 2 * i + 2

        # Get the current effective path sum from each child to its deepest leaf.
        # These values in the `cost` array have already been updated by previous
        # iterations (for deeper nodes) to represent the maximum path sum from
        # that child node down to any leaf in its subtree, after necessary additions
        # within that subtree have been accounted for.
        left_child_path_sum = cost[left_child_idx]
        right_child_path_sum = cost[right_child_idx]

        # To make the paths from the current node 'i' through its children equal,
        # we must ensure that the path sums from its children downwards are equal.
        # We achieve this by increasing the cost of the child node (or nodes)
        # that lead to a smaller path sum, until both paths are equal to the maximum.
        max_child_path_sum = max(left_child_path_sum, right_child_path_sum)

        # Calculate how much needs to be added to each child's path to match the maximum.
        # This difference is added to our running total_added_cost.
        total_added_cost += (max_child_path_sum - left_child_path_sum)
        total_added_cost += (max_child_path_sum - right_child_path_sum)

        # Update the current node's cost. This is the dynamic programming step.
        # The cost of node 'i' now effectively represents the sum of its original cost
        # plus the maximum path sum from its children's subtrees (after equalization).
        # This updated value will be used when its parent node processes it.
        cost[i] += max_child_path_sum
        
    return total_added_cost
