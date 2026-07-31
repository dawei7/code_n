class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root
        for character in word:
            node = node.setdefault(character, {})
        node[None] = {}

    def _find(self, text: str):
        node = self.root
        for character in text:
            if character not in node:
                return None
            node = node[character]
        return node

    def search(self, word: str) -> bool:
        node = self._find(word)
        return node is not None and None in node

    def startsWith(self, prefix: str) -> bool:
        return self._find(prefix) is not None


def solve(operations: list[list[str]]) -> list[bool]:
    trie = Trie()
    results: list[bool] = []
    for operation, value in operations:
        if operation == "insert":
            trie.insert(value)
        elif operation == "search":
            results.append(trie.search(value))
        elif operation == "startsWith":
            results.append(trie.startsWith(value))
        else:
            raise ValueError(f"unknown operation: {operation}")
    return results
