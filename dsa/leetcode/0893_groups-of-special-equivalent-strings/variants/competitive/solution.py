from typing import List


class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        signatures = set()
        for word in words:
            counts = [0] * 52
            for index, character in enumerate(word):
                offset = 26 if index % 2 else 0
                counts[offset + ord(character) - ord("a")] += 1
            signatures.add(tuple(counts))
        return len(signatures)
