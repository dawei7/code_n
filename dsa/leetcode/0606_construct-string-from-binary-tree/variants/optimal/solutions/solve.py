class TreeNode:
    """Local equivalent of the binary-tree node supplied by LeetCode's judge."""

    def __init__(
        self,
        val: int = 0,
        left: "TreeNode | None" = None,
        right: "TreeNode | None" = None,
    ):
        self.val = val
        self.left = left
        self.right = right


def solve(root: TreeNode | None) -> str:
    if root is None:
        return ""

    tokens = []
    actions = [("node", root)]

    while actions:
        action, value = actions.pop()
        if action == "text":
            tokens.append(value)
            continue

        node = value
        tokens.append(str(node.val))

        if node.right is not None:
            actions.append(("text", ")"))
            actions.append(("node", node.right))
            actions.append(("text", "("))

            actions.append(("text", ")"))
            if node.left is not None:
                actions.append(("node", node.left))
            actions.append(("text", "("))
        elif node.left is not None:
            actions.append(("text", ")"))
            actions.append(("node", node.left))
            actions.append(("text", "("))

    return "".join(tokens)
