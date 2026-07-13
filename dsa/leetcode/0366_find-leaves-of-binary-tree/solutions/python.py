"""Optimal solution for LeetCode 366: Find Leaves of Binary Tree."""


def solve(root) -> list[list[int]]:
    rounds: list[list[int]] = []

    def leaf_height(node) -> int:
        if node is None:
            return -1
        height = 1 + max(leaf_height(node.left), leaf_height(node.right))
        if height == len(rounds):
            rounds.append([])
        rounds[height].append(node.val)
        return height

    leaf_height(root)
    return rounds

