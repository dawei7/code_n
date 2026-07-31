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
        binary = TreeNode(root.val)
        previous = None
        for child in root.children:
            encoded_child = self.encode(child)
            if previous is None:
                binary.left = encoded_child
            else:
                previous.right = encoded_child
            previous = encoded_child
        return binary

    def decode(self, data: TreeNode | None) -> Node | None:
        if data is None:
            return None
        children = []
        child = data.left
        while child is not None:
            children.append(self.decode(child))
            child = child.right
        return Node(data.val, children)


def solve(root: Node | None) -> Node | None:
    codec = Codec()
    return codec.decode(codec.encode(root))
