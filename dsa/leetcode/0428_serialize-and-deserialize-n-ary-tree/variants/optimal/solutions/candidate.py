"""Inert review candidate for LeetCode 428."""


class Node:
    """Local equivalent of LeetCode's Node for the standalone app template."""

    def __init__(self, val: int = 0, children: "list[Node] | None" = None):
        self.val = val
        self.children = [] if children is None else children


class Codec:
    def serialize(self, root: Node | None) -> str:
        if root is None:
            return "#"

        tokens: list[str] = []
        stack = [root]
        while stack:
            node = stack.pop()
            tokens.append(str(node.val))
            tokens.append(str(len(node.children)))
            stack.extend(reversed(node.children))
        return " ".join(tokens)

    def deserialize(self, data: str) -> Node | None:
        if data == "#":
            return None

        tokens = data.split()
        root = Node(int(tokens[0]))
        stack: list[tuple[Node, int]] = [(root, int(tokens[1]))]
        position = 2

        while stack:
            parent, remaining_children = stack.pop()
            if remaining_children == 0:
                continue

            child = Node(int(tokens[position]))
            child_count = int(tokens[position + 1])
            position += 2
            parent.children.append(child)
            stack.append((parent, remaining_children - 1))
            stack.append((child, child_count))

        return root


def solve(root: Node | None) -> Node | None:
    codec = Codec()
    return codec.deserialize(codec.serialize(root))
