from collections import Counter
from typing import List


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        word_count = len(words)
        frequencies = Counter(character for word in words for character in word)
        return all(count % word_count == 0 for count in frequencies.values())
