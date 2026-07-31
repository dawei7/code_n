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
        values = []

        def preorder(node: TreeNode | None) -> None:
            if node is None:
                return
            values.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return " ".join(values)

    def deserialize(self, data: str) -> TreeNode | None:
        values = [int(token) for token in data.split()]
        index = 0

        def build(lower: float, upper: float) -> TreeNode | None:
            nonlocal index
            if index == len(values) or not lower < values[index] < upper:
                return None
            value = values[index]
            index += 1
            node = TreeNode(value)
            node.left = build(lower, value)
            node.right = build(value, upper)
            return node

        return build(float("-inf"), float("inf"))


def solve(root: TreeNode | None) -> TreeNode | None:
    codec = Codec()
    return codec.deserialize(codec.serialize(root))
