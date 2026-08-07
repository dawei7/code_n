from collections import Counter


class Solution:
    def minimumKeypresses(self, s: str) -> int:
        frequencies = sorted(Counter(s).values(), reverse=True)
        return sum(frequency * (index // 9 + 1) for index, frequency in enumerate(frequencies))
