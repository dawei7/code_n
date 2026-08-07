class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        frequencies = [0] * 26
        for character in s:
            frequencies[ord(character) - ord("a")] += 1

        target = next(count for count in frequencies if count)
        return all(count == 0 or count == target for count in frequencies)
