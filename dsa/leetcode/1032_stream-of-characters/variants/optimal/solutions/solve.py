"""Optimal app-local solution for LeetCode 1032."""

from collections import deque


class StreamChecker:
    def __init__(self, words):
        self.trie = {}
        self.max_length = max(len(word) for word in words)
        for word in words:
            node = self.trie
            for character in reversed(word):
                node = node.setdefault(character, {})
            node["$"] = {}
        self.stream = deque(maxlen=self.max_length)

    def query(self, letter):
        self.stream.append(letter)
        node = self.trie
        for character in reversed(self.stream):
            if character not in node:
                return False
            node = node[character]
            if "$" in node:
                return True
        return False


def solve(words, queries):
    checker = StreamChecker(words)
    return [checker.query(character) for character in queries]
