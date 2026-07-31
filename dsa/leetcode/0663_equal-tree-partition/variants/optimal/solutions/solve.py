def solve(root) -> bool:
    subtree_sums = []

    def total(node):
        if node is None:
            return 0
        value = node.val + total(node.left) + total(node.right)
        subtree_sums.append(value)
        return value

    tree_sum = total(root)
    subtree_sums.pop()
    return tree_sum % 2 == 0 and tree_sum // 2 in subtree_sums
