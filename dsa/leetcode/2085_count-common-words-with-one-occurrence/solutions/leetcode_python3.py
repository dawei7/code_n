from collections import Counter
from typing import List


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        counts1 = Counter(words1)
        counts2 = Counter(words2)
        return sum(
            counts1[word] == 1 and counts2[word] == 1
            for word in counts1
        )
