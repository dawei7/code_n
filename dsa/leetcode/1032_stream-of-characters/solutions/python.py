class StreamChecker:
    def __init__(self, words: list[str]):
        self.trie: dict[str, dict] = {}
        self.max_len = 0
        for word in words:
            self.max_len = max(self.max_len, len(word))
            node = self.trie
            for char in reversed(word):
                node = node.setdefault(char, {})
            node["$"] = {}
        self.stream: list[str] = []

    def query(self, letter: str) -> bool:
        self.stream.append(letter)
        if len(self.stream) > self.max_len:
            self.stream.pop(0)

        node = self.trie
        for char in reversed(self.stream):
            if char not in node:
                return False
            node = node[char]
            if "$" in node:
                return True
        return False


def solve(words: list[str], queries: list[str]) -> list[bool]:
    checker = StreamChecker(words)
    return [checker.query(char) for char in queries]
