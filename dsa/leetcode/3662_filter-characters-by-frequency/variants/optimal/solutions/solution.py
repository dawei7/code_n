from collections import Counter


class Solution:
    def filterCharacters(self, s: str, k: int) -> str:
        frequency = Counter(s)
        return "".join(character for character in s if frequency[character] < k)
