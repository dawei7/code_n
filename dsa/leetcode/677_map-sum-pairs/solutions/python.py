class _TrieNode:
    def __init__(self):
        self.children = {}
        self.total = 0


class MapSum:
    def __init__(self):
        self.root = _TrieNode()
        self.values = {}

    def insert(self, key: str, value: int) -> None:
        delta = value - self.values.get(key, 0)
        self.values[key] = value
        node = self.root
        node.total += delta
        for character in key:
            node = node.children.setdefault(character, _TrieNode())
            node.total += delta

    def sum(self, prefix: str) -> int:
        node = self.root
        for character in prefix:
            node = node.children.get(character)
            if node is None:
                return 0
        return node.total


def solve(operations: list[str], arguments: list[list]) -> list[int | None]:
    mapping = None
    output = []
    for operation, args in zip(operations, arguments):
        if operation == "MapSum":
            mapping = MapSum()
            output.append(None)
        elif operation == "insert":
            assert mapping is not None
            mapping.insert(args[0], args[1])
            output.append(None)
        elif operation == "sum":
            assert mapping is not None
            output.append(mapping.sum(args[0]))
        else:
            raise ValueError(f"unknown operation: {operation}")
    return output

