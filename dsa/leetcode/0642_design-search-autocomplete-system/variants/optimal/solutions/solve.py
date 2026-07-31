from collections import Counter


class TrieNode:
    def __init__(self):
        self.children = {}
        self.hot = []


class AutocompleteSystem:
    def __init__(self, sentences: list[str], times: list[int]):
        self.frequency = Counter()
        for sentence, count in zip(sentences, times):
            self.frequency[sentence] += count

        self.root = TrieNode()
        for sentence in self.frequency:
            self.insert(sentence)
        self.current = ""
        self.node = self.root

    def refresh(self, node, sentence):
        if sentence not in node.hot:
            node.hot.append(sentence)
        node.hot.sort(key=lambda candidate: (-self.frequency[candidate], candidate))
        del node.hot[3:]

    def insert(self, sentence):
        node = self.root
        for character in sentence:
            node = node.children.setdefault(character, TrieNode())
            self.refresh(node, sentence)

    def input(self, c: str) -> list[str]:
        if c == "#":
            self.frequency[self.current] += 1
            self.insert(self.current)
            self.current = ""
            self.node = self.root
            return []

        self.current += c
        if self.node is not None:
            self.node = self.node.children.get(c)
        return [] if self.node is None else list(self.node.hot)


def solve(operations: list[str], arguments: list[list[object]]) -> list[object]:
    system: AutocompleteSystem | None = None
    output: list[object] = []
    for operation, args in zip(operations, arguments):
        if operation == "AutocompleteSystem":
            system = AutocompleteSystem(*args)
            output.append(None)
        else:
            output.append(system.input(*args))
    return output
