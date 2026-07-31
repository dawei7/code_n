"""Iterative preorder codec for LeetCode 297."""


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


class Codec:
    def serialize(self, root: TreeNode | None) -> str:
        tokens = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node is None:
                tokens.append("#")
                continue
            tokens.append(str(node.val))
            stack.append(node.right)
            stack.append(node.left)
        return ",".join(tokens)

    def deserialize(self, data: str) -> TreeNode | None:
        tokens = data.split(",")
        if tokens[0] == "#":
            return None
        root = TreeNode(int(tokens[0]))
        stack = [(root, 0)]
        for token in tokens[1:]:
            child = None if token == "#" else TreeNode(int(token))
            parent, slot = stack[-1]
            if slot == 0:
                parent.left = child
                stack[-1] = (parent, 1)
            else:
                parent.right = child
                stack.pop()
            if child is not None:
                stack.append((child, 0))
        return root


def solve(root: TreeNode | None) -> TreeNode | None:
    codec = Codec()
    return codec.deserialize(codec.serialize(root))
