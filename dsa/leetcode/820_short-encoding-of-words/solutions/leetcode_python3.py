from typing import List


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        root = {}
        terminals = []

        for word in set(words):
            node = root
            for character in reversed(word):
                node = node.setdefault(character, {})
            terminals.append((node, len(word)))

        return sum(length + 1 for node, length in terminals if not node)
