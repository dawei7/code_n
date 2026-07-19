from typing import List


class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        trie = {}
        terminal = "#"

        for word in words:
            node = trie
            for character in word:
                node = node.setdefault(character, {})
            node[terminal] = True

        pairs = []
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
