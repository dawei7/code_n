from typing import List


class Solution:
    def countPairs(self, words: List[str]) -> int:
        pairs = 0
        seen = {}

        for word in words:
            first = ord(word[0])
            key = tuple((ord(character) - first) % 26 for character in word)
            pairs += seen.get(key, 0)
            seen[key] = seen.get(key, 0) + 1

        return pairs
