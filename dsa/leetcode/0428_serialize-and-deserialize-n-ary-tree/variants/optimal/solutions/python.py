"""Optimal app-local round-trip codec for LeetCode 428."""


def solve(tree):
    def serialize(root) -> str:
        if root is None:
            return "#"
        tokens: list[str] = []

        def encode(node) -> None:
            value, children = node
            tokens.append(str(value))
            tokens.append(str(len(children)))
            for child in children:
                encode(child)

        encode(root)
        return " ".join(tokens)

    def deserialize(data: str):
        if data == "#":
            return None
        tokens = iter(data.split())

        def decode():
            value = int(next(tokens))
            child_count = int(next(tokens))
            return [value, [decode() for _ in range(child_count)]]

        return decode()

    return deserialize(serialize(tree))
