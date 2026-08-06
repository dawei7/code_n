"""Trie-guided word-break dynamic programming for LeetCode 472."""


class TrieNode:
    """A dictionary-prefix state."""

    __slots__ = ("children", "is_word")

    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.is_word = False


def solve(words: list[str]) -> list[str]:
    root = TrieNode()
    concatenated: list[str] = []

    def insert(word: str) -> None:
        node = root
        for c in word:
            child = node.children.get(c)
            if child is None:
                child = TrieNode()
                node.children[c] = child
            node = child
        node.is_word = True

    for word in sorted(words, key=len):
        if not word:
            continue
        length = len(word)
        reachable = [False] * (length + 1)
        reachable[0] = True

        for start in range(length):
            if not reachable[start]:
                continue
            node = root
            for end in range(start, length):
                node = node.children.get(word[end])
                if node is None:
                    break
                if node.is_word:
                    reachable[end + 1] = True
            if reachable[-1]:
                break

        if reachable[-1]:
            concatenated.append(word)
        insert(word)

    return concatenated
