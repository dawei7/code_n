def solve(root) -> int:
    minimum = root.val

    def second_in_subtree(node) -> int:
        if node is None:
            return -1
        if node.val > minimum:
            return node.val

        left = second_in_subtree(node.left)
        right = second_in_subtree(node.right)
        if left == -1:
            return right
        if right == -1:
            return left
        return min(left, right)

    return second_in_subtree(root)

