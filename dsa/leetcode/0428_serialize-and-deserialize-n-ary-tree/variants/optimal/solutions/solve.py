class Node:
    """Local equivalent of LeetCode's Node for the standalone app template."""

    def __init__(self, val: int = 0, children: "list[Node] | None" = None):
        self.val = val
        self.children = [] if children is None else children


class Codec:
    def serialize(self, root: Node | None) -> str:
        if root is None:
            return "#"
        tokens = []

        def encode(node: Node) -> None:
            tokens.append(str(node.val))
            tokens.append(str(len(node.children)))
            for child in node.children:
                encode(child)

        encode(root)
        return " ".join(tokens)

    def deserialize(self, data: str) -> Node | None:
        if data == "#":
            return None
        tokens = iter(data.split())

        def decode() -> Node:
            value = int(next(tokens))
            child_count = int(next(tokens))
            return Node(value, [decode() for _ in range(child_count)])

        return decode()


def solve(root: Node | None) -> Node | None:
    codec = Codec()
    return codec.deserialize(codec.serialize(root))
