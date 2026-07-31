class TreeNode:
    """Local equivalent of LeetCode's TreeNode for the standalone app template."""

    def __init__(
        self,
        val: int = 0,
        left: "TreeNode | None" = None,
        right: "TreeNode | None" = None,
    ):
        self.val = val
        self.left = left
        self.right = right


def solve(root, p, q):
    def search(node):
        if node is None:
            return None, 0

        left_candidate, left_found = search(node.left)
        right_candidate, right_found = search(node.right)
        found = left_found + right_found + (node is p) + (node is q)

        if left_candidate is not None and right_candidate is not None:
            candidate = node
        elif node is p or node is q:
            candidate = node
        else:
            candidate = left_candidate or right_candidate
        return candidate, found

    candidate, found = search(root)
    return candidate if found == 2 else None
