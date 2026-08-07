from typing import List


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        terminal = "#"
        trie = {}
        for root in dictionary:
            node = trie
            for character in root:
                node = node.setdefault(character, {})
            node[terminal] = True

        def replacement(word):
            node = trie
            for index, character in enumerate(word):
                if character not in node:
                    return word
                node = node[character]
                if terminal in node:
                    return word[: index + 1]
            return word

        return " ".join(replacement(word) for word in sentence.split())
