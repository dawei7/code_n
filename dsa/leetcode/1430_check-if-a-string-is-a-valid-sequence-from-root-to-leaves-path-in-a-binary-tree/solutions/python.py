"""Optimal app-local solution for LeetCode 1430."""


def solve(root, arr: list[int]) -> bool:
    def matches(node, index: int) -> bool:
        if node is None or index == len(arr) or node.val != arr[index]:
            return False
        if node.left is None and node.right is None:
            return index == len(arr) - 1
        return matches(node.left, index + 1) or matches(node.right, index + 1)

    return matches(root, 0)
