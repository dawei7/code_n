class _TrieNode:
    def __init__(self):
        self.children = {}
        self.total = 0


class MapSum:
    def __init__(self):
        self.root = _TrieNode()
        self.values = {}

    def insert(self, key: str, val: int) -> None:
        delta = val - self.values.get(key, 0)
        self.values[key] = val
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

