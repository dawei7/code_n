"""Inert review candidate for LeetCode 431."""


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


class Node:
    """Local equivalent of LeetCode's Node for the standalone app template."""

    def __init__(self, val: int = 0, children: "list[Node] | None" = None):
        self.val = val
        self.children = [] if children is None else children


class Codec:
    def encode(self, root: Node | None) -> TreeNode | None:
        if root is None:
            return None

        binary_root = TreeNode(root.val)
        stack: list[tuple[Node, TreeNode, int, TreeNode | None]] = [
            (root, binary_root, 0, None)
        ]
        while stack:
            node, binary, child_index, previous = stack.pop()
            if child_index == len(node.children):
                continue

            child = node.children[child_index]
            encoded_child = TreeNode(child.val)
            if previous is None:
                binary.left = encoded_child
            else:
                previous.right = encoded_child

            stack.append((node, binary, child_index + 1, encoded_child))
            stack.append((child, encoded_child, 0, None))
        return binary_root

    def decode(self, data: TreeNode | None) -> Node | None:
        if data is None:
            return None

        root = Node(data.val)
        stack: list[tuple[Node, TreeNode | None]] = [(root, data.left)]
        while stack:
            parent, child = stack.pop()
            if child is None:
                continue

            decoded_child = Node(child.val)
            parent.children.append(decoded_child)
            stack.append((parent, child.right))
            stack.append((decoded_child, child.left))
        return root


def solve(root: Node | None) -> Node | None:
    codec = Codec()
    return codec.decode(codec.encode(root))
