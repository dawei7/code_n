class Codec:
    def serialize(self, root: 'Node') -> str:
        if root is None:
            return "#"
        tokens = []

        def encode(node: 'Node') -> None:
            tokens.append(str(node.val))
            tokens.append(str(len(node.children)))
            for child in node.children:
                encode(child)

        encode(root)
        return " ".join(tokens)

    def deserialize(self, data: str) -> 'Node':
        if data == "#":
            return None
        tokens = iter(data.split())

        def decode() -> 'Node':
            value = int(next(tokens))
            child_count = int(next(tokens))
            return Node(value, [decode() for _ in range(child_count)])

        return decode()
