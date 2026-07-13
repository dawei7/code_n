from collections import Counter


class TrieNode:
    def __init__(self):
        self.children: dict[str, TrieNode] = {}
        self.hot: list[str] = []


class AutocompleteSystem:
    def __init__(self, sentences: list[str], times: list[int]):
        self._frequency: Counter[str] = Counter()
        for sentence, count in zip(sentences, times):
            self._frequency[sentence] += count

        self._root = TrieNode()
        for sentence in self._frequency:
            self._insert(sentence)
        self._current = ""
        self._node: TrieNode | None = self._root

    def _refresh(self, node: TrieNode, sentence: str) -> None:
        if sentence not in node.hot:
            node.hot.append(sentence)
        node.hot.sort(key=lambda candidate: (-self._frequency[candidate], candidate))
        del node.hot[3:]

    def _insert(self, sentence: str) -> None:
        node = self._root
        for character in sentence:
            node = node.children.setdefault(character, TrieNode())
            self._refresh(node, sentence)

    def input(self, character: str) -> list[str]:
        if character == "#":
            self._frequency[self._current] += 1
            self._insert(self._current)
            self._current = ""
            self._node = self._root
            return []

        self._current += character
        if self._node is not None:
            self._node = self._node.children.get(character)
        return [] if self._node is None else list(self._node.hot)


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
