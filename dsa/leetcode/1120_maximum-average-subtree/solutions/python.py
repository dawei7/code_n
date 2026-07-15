"""Optimal app-local solution for LeetCode 1120."""


def solve(root):
    best = 0.0

    def summarize(node):
        nonlocal best
        if node is None:
            return 0, 0
        left_sum, left_count = summarize(node.left)
        right_sum, right_count = summarize(node.right)
        total = node.val + left_sum + right_sum
        count = 1 + left_count + right_count
        best = max(best, total / count)
        return total, count

    summarize(root)
    return best
