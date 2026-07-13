from typing import List


class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.count = 0


class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        roots = {}
        for word in words:
            signature = (len(word), word[0], word[-1])
            node = roots.setdefault(signature, TrieNode())
            for character in word:
                node = node.children.setdefault(character, TrieNode())
                node.count += 1

        answer = []
        for word in words:
            node = roots[(len(word), word[0], word[-1])]
            prefix_length = 0
            for character in word:
                node = node.children[character]
                prefix_length += 1
                if node.count == 1:
                    break

            omitted = len(word) - prefix_length - 1
            if omitted <= 1:
                answer.append(word)
            else:
                answer.append(f"{word[:prefix_length]}{omitted}{word[-1]}")
        return answer
