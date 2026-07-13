from collections import Counter


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        frequencies = Counter(s)
        pieces = []
        for character in order:
            pieces.append(character * frequencies.pop(character, 0))
        for character, frequency in frequencies.items():
            pieces.append(character * frequency)
        return "".join(pieces)
