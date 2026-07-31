from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root = TrieNode()

        for word in words:
            node = root
            for character in word:
                if character not in node.children:
                    node.children[character] = TrieNode()
                node = node.children[character]
                node.count += 1

        answer = []
        for word in words:
            node = root
            score = 0
            for character in word:
                node = node.children[character]
                score += node.count
            answer.append(score)
        return answer
