class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: "TreeNode | None" = None,
        right: "TreeNode | None" = None,
    ):
        self.val = val
        self.left = left
        self.right = right


def solve(trees: list[TreeNode]) -> TreeNode | None:
    roots = {tree.val: tree for tree in trees}
    leaf_values = set()
    for tree in trees:
        if tree.left:
            leaf_values.add(tree.left.val)
        if tree.right:
            leaf_values.add(tree.right.val)

    candidates = [tree for tree in trees if tree.val not in leaf_values]
    if len(candidates) != 1:
        return None

    root = candidates[0]
    roots.pop(root.val)
    stack = [(root, float("-inf"), float("inf"))]

    while stack:
        node, lower, upper = stack.pop()
        if not lower < node.val < upper:
            return None

        if node.left is None and node.right is None and node.val in roots:
            graft = roots.pop(node.val)
            node.left = graft.left
            node.right = graft.right

        if node.left:
            stack.append((node.left, lower, node.val))
        if node.right:
            stack.append((node.right, node.val, upper))

    return root if not roots else None
