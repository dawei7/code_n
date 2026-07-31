class RopeTreeNode:
    """Local equivalent of LeetCode's RopeTreeNode model."""

    def __init__(
        self,
        len: int = 0,
        val: str = "",
        left: "RopeTreeNode | None" = None,
        right: "RopeTreeNode | None" = None,
    ):
        self.len = len
        self.val = val
        self.left = left
        self.right = right


def solve(root: RopeTreeNode, k: int) -> str:
    node = root

    while node.val == "":
        if node.left is None:
            left_length = 0
        elif node.left.len > 0:
            left_length = node.left.len
        else:
            left_length = len(node.left.val)

        if k <= left_length:
            node = node.left
        else:
            k -= left_length
            node = node.right

    return node.val[k - 1]
