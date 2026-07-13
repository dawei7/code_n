from typing import Optional


class Codec:
    def serialize(self, root: Optional['TreeNode']) -> str:
        values = []

        def preorder(node: Optional['TreeNode']) -> None:
            if node is None:
                return
            values.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return " ".join(values)

    def deserialize(self, data: str) -> Optional['TreeNode']:
        values = [int(token) for token in data.split()]
        index = 0

        def build(lower: float, upper: float) -> Optional['TreeNode']:
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
