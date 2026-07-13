def solve(root) -> int:
    longest = 0

    def downward(node) -> int:
        nonlocal longest
        if node is None:
            return 0

        left_length = downward(node.left)
        right_length = downward(node.right)
        left_arm = 0
        right_arm = 0

        if node.left is not None and node.left.val == node.val:
            left_arm = left_length + 1
        if node.right is not None and node.right.val == node.val:
            right_arm = right_length + 1

        longest = max(longest, left_arm + right_arm)
        return max(left_arm, right_arm)

    downward(root)
    return longest

