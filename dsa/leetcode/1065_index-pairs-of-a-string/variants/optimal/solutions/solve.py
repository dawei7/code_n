"""Optimal solution for LeetCode 1065: Index Pairs of a String."""


def solve(text: str, words: list[str]) -> list[list[int]]:
    trie: dict = {}
    terminal = "#"

    for word in words:
        node = trie
        for character in word:
            node = node.setdefault(character, {})
        node[terminal] = True

    pairs: list[list[int]] = []
    for start in range(len(text)):
        node = trie
        for end in range(start, len(text)):
            character = text[end]
            if character not in node:
                break
            node = node[character]
            if terminal in node:
                pairs.append([start, end])
    return pairs
