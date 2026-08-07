from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        frequencies = Counter(s)
        buckets = [[] for _ in range(len(s) + 1)]
        for character, frequency in frequencies.items():
            buckets[frequency].append(character)

        pieces = []
        for frequency in range(len(s), 0, -1):
            for character in buckets[frequency]:
                pieces.append(character * frequency)
        return "".join(pieces)
